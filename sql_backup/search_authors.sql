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

 Date: 11/05/2018 17:01:35
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for search_authors
-- ----------------------------
DROP TABLE IF EXISTS `search_authors`;
CREATE TABLE `search_authors`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uniid` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sex` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `organization` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `avatar_src` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `work_experience` varchar(250) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `edu_experience` varchar(250) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `domain` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `intro` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of search_authors
-- ----------------------------
INSERT INTO `search_authors` VALUES (1, 'UPQ2oUMJesA', '王万良', '男', '浙江工业大学', 'https://gss0.bdstatic.com/-4o3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/sign=92b8090abd003af349badb62052bc619/e4dde71190ef76c6038412289616fdfaaf51675b.jpg', '浙江工业大学,https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=f883c30d257f9e2f70351a0e270b8e19/35a85edf8db1cb13105c4df8df54564e92584b27.jpg', '浙江工业大学,https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=f883c30d257f9e2f70351a0e270b8e19/35a85edf8db1cb13105c4df8df54564e92584b27.jpg', '计算机智能自动化,人工智能', '王万良，男，江苏高邮市人，博士，1997年晋升浙江工业大学教授，2008年入选国家级教学名师，2014年入选国家首批“万人计划”教学名师');
INSERT INTO `search_authors` VALUES (2, 'Ilv4tKNpdzA', '王万良', '男', '首都师范大学', 'https://gss1.bdstatic.com/-vo3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/sign=7555f1730cf3d7ca08f63874c21ebe3c/ac345982b2b7d0a2e183b2d0cbef76094b369a31.jpg', '首都师范大学,https://www.scholarmate.com/insLogo/1503.jpg', '首都师范大学,https://www.scholarmate.com/insLogo/1503.jpg', '信息技术', '王万良， 男，1948年1月28日出生， 中共党员，教授，博士生导师，首都师范大学副校长。');
INSERT INTO `search_authors` VALUES (3, 'JvUzHyT72BGInoTrNAOM3aQ', '龚卫华', '男', '浙江工业大学', 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2766636815,3165673923&fm=27&gp=0.jpg', '浙江工业大学,https://www.scholarmate.com/insLogo/1544.jpg', '华中科技大学,https://www.scholarmate.com/insLogo/779.jpg', '数据挖掘,P2P计算', '龚卫华,男,1977年生,博士,副教授,硕士生导师。');
INSERT INTO `search_authors` VALUES (4, 'BBd8X5gl31Oj2RJ6P1cipA', '姚信威', '男', '浙江工业大学', 'http://www.escience.cn/system/img?imgId=80017', '浙江工业大学,https://www.scholarmate.com/insLogo/1544.jpg', '浙江工业大学,https://www.scholarmate.com/insLogo/1544.jpg', '数据挖掘,物联网,网络优化,太赫兹通信,纳米网络', '姚信威，男，入选浙江工业大学首批校聘副教授');
INSERT INTO `search_authors` VALUES (5, 'BBd8X5gl31NcqaL4AU1nhQ', '郑建炜', '男', '浙江工业大学', 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2766636815,3165673923&fm=27&gp=0.jpg', '浙江工业大学,https://www.scholarmate.com/insLogo/1544.jpg', '浙江工业大学,https://www.scholarmate.com/insLogo/1544.jpg', '人工智能,模式识别,媒体目标跟踪', '郑建炜,男,工学博士,讲师,1982年3月出生。2010年6月获得浙江工业大学工学博士学位(导师:王万良教授)。');
INSERT INTO `search_authors` VALUES (6, 'thxMLiZ2TRbrUS24CammJQ', '徐新黎', '女', '浙江工业大学', 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2766636815,3165673923&fm=27&gp=0.jpg', '浙江工业大学,https://www.scholarmate.com/insLogo/1544.jpg', '浙江工业大学,https://www.scholarmate.com/insLogo/1544.jpg', '人工智能,粒子群算法,动态规划,车间调度', '徐新黎,女,1977年出生,浙江余姚人。');
INSERT INTO `search_authors` VALUES (7, 'k2By2BHpfOQiUIJtkx0NfJ7Q', '蒋一波', '男', '浙江工业大学', 'http://www.jwc.zjut.edu.cn/UploadFile/images/201404290845479.jpg', '浙江工业大学,https://www.scholarmate.com/insLogo/1544.jpg', '浙江工业大学,https://www.scholarmate.com/insLogo/1544.jpg', '无线传感网,大数据分析', '蒋一波老师2008年博士毕业，任职于浙江工业大学、软件学院。2010年任职于浙江工业大学、计算机科学与技术学院。');
INSERT INTO `search_authors` VALUES (8, 'gdC9pv0cs2BsWtCOpJd4RAg', '管秋', '女', '浙江工业大学', 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2766636815,3165673923&fm=27&gp=0.jpg', '浙江工业大学,https://www.scholarmate.com/insLogo/1544.jpg', '浙江工业大学,https://www.scholarmate.com/insLogo/1544.jpg', '三维建模,医学图像分析,计算机视觉,图像理解', '管秋,女，1972年出生，博士，教授，硕士生导师。');
INSERT INTO `search_authors` VALUES (9, 'thxMLiZ2TRbpGVbK5VHB8Q', '范兴刚', '男', '浙江工业大学', 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2766636815,3165673923&fm=27&gp=0.jpg', '浙江工业大学,https://www.scholarmate.com/insLogo/1544.jpg', '浙江大学,https://www.scholarmate.com/insLogo/1541.jpg', '无线传感网络,网络通信', '范兴刚 男 ,1974年5月出生，中共党员 博士（浙江大学）。浙江工业大学计算机科学与技术学院副教授，工学博士，发表国际国内论文十多篇。');

SET FOREIGN_KEY_CHECKS = 1;