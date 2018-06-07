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

 Date: 07/06/2018 14:50:18
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for search_users
-- ----------------------------
DROP TABLE IF EXISTS `search_users`;
CREATE TABLE `search_users`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `right_type` varchar(4) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of search_users
-- ----------------------------
INSERT INTO `search_users` VALUES (1, 'admin', 'admin', '1');

SET FOREIGN_KEY_CHECKS = 1;
