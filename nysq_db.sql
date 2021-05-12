-- nyse.price_data definition

CREATE TABLE `price_data` (
  `date` date DEFAULT NULL,
  `open` double DEFAULT NULL,
  `high` double DEFAULT NULL,
  `low` double DEFAULT NULL,
  `close` double DEFAULT NULL,
  `volume` bigint(20) DEFAULT NULL,
  `ticker` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- nyse.security_master definition

CREATE TABLE `security_master` (
  `ticker` varchar(50) DEFAULT NULL,
  `short_name` varchar(1000) DEFAULT NULL,
  `long_name` varchar(1000) DEFAULT NULL,
  `sector` varchar(1000) DEFAULT NULL,
  `industry` varchar(1000) DEFAULT NULL,
  `address1` varchar(1000) DEFAULT NULL,
  `city` varchar(1000) DEFAULT NULL,
  `state` varchar(1000) DEFAULT NULL,
  `zip` varchar(1000) DEFAULT NULL,
  `phone` varchar(1000) DEFAULT NULL,
  `website` varchar(1000) DEFAULT NULL,
  `dividend_rate` double(40,2) DEFAULT NULL,
  `fifty_day_average` float(10,2) DEFAULT NULL,
  `currency` varchar(50) DEFAULT NULL,
  `market_cap` bigint(20) DEFAULT NULL,
  `average_volume` bigint(20) DEFAULT NULL,
  `shares_outstanding` bigint(20) DEFAULT NULL,
  `total_price_points` int(11) DEFAULT NULL,
  `start_date` varchar(100) DEFAULT NULL,
  `end_date` varchar(100) DEFAULT NULL,
  `daily_avg_returns` float(10,4) DEFAULT NULL,
  `weekly_avg_returns` float(10,4) DEFAULT NULL,
  `monthly_avg_returns` float(10,4) DEFAULT NULL,
  `daily_volatility` float(10,4) DEFAULT NULL,
  `weekly_volatility` float(10,4) DEFAULT NULL,
  `monthly_volatility` float(10,4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- nyse.user_login definition

CREATE TABLE `user_login` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1009 DEFAULT CHARSET=utf8mb4;


-- nyse.user_profile definition

CREATE TABLE `user_profile` (
  `user_id` int(11) DEFAULT NULL,
  `risk_apt` float DEFAULT NULL,
  `yearly_inv` bigint(20) DEFAULT NULL,
  `exp_return` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- nyse.weekly_data definition

CREATE TABLE `weekly_data` (
  `ticker` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `price` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;