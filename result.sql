/*
 Navicat Premium Data Transfer

 Source Server         : tencent_pubg
 Source Server Type    : MySQL
 Source Server Version : 50724
 Source Host           : 118.25.17.119:3306
 Source Schema         : tencent_migrate

 Target Server Type    : MySQL
 Target Server Version : 50724
 File Encoding         : 65001

 Date: 09/01/2019 11:00:36
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for result
-- ----------------------------
DROP TABLE IF EXISTS `result`;
CREATE TABLE `result` (
  `date` varchar(8) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '迁徙日期',
  `dep_citycode` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '出发地城市代码',
  `departure` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '出发地',
  `des_citycode` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '目的地城市代码',
  `destination` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '目的地',
  `total` int(255) NOT NULL COMMENT '总迁出人数',
  `heatvalue` float(4,1) NOT NULL COMMENT '热度值',
  `bus_persontime` int(255) NOT NULL COMMENT '公交车人次',
  `bus_proportion` float(2,2) NOT NULL COMMENT '公交车百分比',
  `train_persontime` int(255) NOT NULL COMMENT '火车人次',
  `train_proportion` float(2,2) NOT NULL COMMENT '火车人次百分比',
  `airplane_persontime` int(11) NOT NULL COMMENT '飞机人次',
  `airplane_proportion` float(2,2) NOT NULL COMMENT '飞机占比',
  PRIMARY KEY (`date`,`dep_citycode`,`des_citycode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

SET FOREIGN_KEY_CHECKS = 1;
