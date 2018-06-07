/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 50721
 Source Host           : localhost:3306
 Source Schema         : sis

 Target Server Type    : MySQL
 Target Server Version : 50721
 File Encoding         : 65001

 Date: 07/06/2018 14:50:02
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for search_organization
-- ----------------------------
DROP TABLE IF EXISTS `search_organization`;
CREATE TABLE `search_organization`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `english_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `location` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `logo` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `website` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `introduction` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of search_organization
-- ----------------------------
INSERT INTO `search_organization` VALUES (1, '浙江工业大学', 'Zhejiang University Of Technology\r\n', '浙江省', 'https://www.scholarmate.com/insLogo/1544.jpg', 'http://www.zjut.edu.cn/', '  浙江工业大学（Zhejiang University of Technology），简称浙工大，是中华人民共和国教育部与浙江省人民政府共建的浙江首批省属重点大学  ，国家“2011计划”首批14所牵头高校，首批“卓越计划”入选高校，亚洲规划院校联盟（APSA）成员，入选国家“111计划”。');

SET FOREIGN_KEY_CHECKS = 1;
