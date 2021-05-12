from pyspark.sql.functions import last_day,col, to_date, min, max, avg, count

# read security data

security_info = spark.read.option("header","True").csv("/user/cloudera/CIS-Project/Stock_Info").drop("_c0")

# read data from price_adta 
price_data = spark.read.format("csv").option("sep",",").option("header","True").load("/user/cloudera/CIS-Project/price_data_2021-05-05.csv").select("Ticker","Date","Close").withColumnRenamed("Close","Price")

price_count = price_data.groupBy("Ticker").agg(count("Date").alias("total_price_points"))

start_date = price_data.groupBy("Ticker").agg(min("Date").alias("start_date"))

end_date = price_data.groupBy("Ticker").agg(max("Date").alias("end_date"))

security_info = security_info.join(price_count, security_info.ticker==price_count.Ticker).drop(price_count.Ticker)
security_info = security_info.join(start_date, security_info.ticker==start_date.Ticker).drop(start_date.Ticker)
security_info = security_info.join(end_date, security_info.ticker==end_date.Ticker).drop(end_date.Ticker)

# calculate average daily return 

price_data.createOrReplaceTempView("price_data")

daily_returns = spark.sql("select Ticker, Date, Price,lead(Date) over (partition by Ticker order by Date) as lead_date,  lead(Price)over(partition by Ticker order by Date) as lead_price, round(((lead(Price)over(partition by ticker order by date)-Price)/Price),4)*100 as return  from price_data wd")

daily_avg_returns = daily_returns.groupBy("Ticker").agg(avg("return"))

security_info = security_info.join(daily_avg_returns, security_info.ticker==daily_avg_returns.Ticker).drop(daily_avg_returns.Ticker).withColumnRenamed("avg(return)","daily_avg_returns")

# calculate average weekly return

weekly_data = spark.sql("select ticker, date, round(cast(Price as float),2) as price from price_data where date = date_add(date_trunc('WEEK',date),4) and date >'2016-05-01' ")

weekly_data.createOrReplaceTempView("weekly_data")

weekly_return = spark.sql("select ticker, date,price,lead(Date) over (partition by ticker order by date) as lead_date,  lead(price)over(partition by ticker order by date) as lead_price, ((lead(price)over(partition by ticker order by date)-price)/price)*100 as return  from weekly_data wd")

weekly_avg_returns = weekly_return.groupBy("Ticker").agg(avg("return"))

security_info = security_info.join(weekly_avg_returns, security_info.ticker==weekly_avg_returns.Ticker).drop(weekly_avg_returns.Ticker).withColumnRenamed("avg(return)","weekly_avg_returns")

# calculate average monthly return

monthly_data = spark.sql("select ticker, date, round(cast(Price as float),2) as price from price_data where date = last_day(date) and date >'2016-05-01'")

monthly_data.createOrReplaceTempView("monthly_data")

monthly_return = spark.sql("select ticker, date,price,lead(Date) over (partition by ticker order by date) as lead_date,  lead(price)over(partition by ticker order by date) as lead_price, ((lead(price)over(partition by ticker order by date)-price)/price)*100 as return  from monthly_data wd")

monthly_avg_returns = monthly_return.groupBy("Ticker").agg(avg("return"))

security_info = security_info.join(monthly_avg_returns, security_info.ticker==monthly_avg_returns.Ticker).drop(monthly_avg_returns.Ticker).withColumnRenamed("avg(return)","monthly_avg_returns")

# daily volatility

daily_volatility = spark.sql("select Ticker, stddev(Price)/sqrt(12) as daily_volatility from price_data group by Ticker")

security_info = security_info.join(daily_volatility, security_info.ticker==daily_volatility.Ticker).drop(daily_volatility.Ticker)

# weekly volatility

weekly_volatility = spark.sql("select Ticker, stddev(Price)/sqrt(sqrt(12)) as weekly_volatility from weekly_data group by Ticker")

security_info = security_info.join(weekly_volatility, security_info.ticker==weekly_volatility.Ticker).drop(weekly_volatility.Ticker)

# monthly volatility

monthly_volatility = spark.sql("select Ticker, stddev(Price)/sqrt(sqrt(12)) as monthly_volatility from monthly_data group by Ticker")

security_info = security_info.join(monthly_volatility, security_info.ticker==monthly_volatility.Ticker).drop(monthly_volatility.Ticker)

# write the security master

security_info.coalesce(1).write.mode("overwrite").option("header","True").csv("/user/cloudera/CIS-Project/security_master")

weekly_data.coalesce(1).write.mode("overwrite").option("header","True").csv("/user/cloudera/CIS-Project/weekly_data")