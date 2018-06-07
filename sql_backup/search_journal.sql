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

 Date: 07/06/2018 14:50:09
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for search_journal
-- ----------------------------
DROP TABLE IF EXISTS `search_journal`;
CREATE TABLE `search_journal`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `website` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `introduction` varchar(800) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `category` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `logo` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `english_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `host_unit` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `influence` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `honor` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of search_journal
-- ----------------------------
INSERT INTO `search_journal` VALUES (1, '计算机学报', 'http://cjc.ict.ac.cn/', '《计算机学报》是中国计算机领域权威性学术刊物。其宗旨是报道中国计算机科学技术领域最高水平的科研成果。它由中国计算机学会与中国科学院计算技术研究所主办、科学出版社出版，以中文编辑形式与读者见面，同时以英文摘要形式向国际各大检索系统提供基本内容介绍。', '核心期刊;SA;JST;EI;CSCD', 'http://c61.cnki.net/CJFD/big/JSJX.jpg', 'Chinese Journal of Computers', '中国科学院计算技术研究所;中国计算机学会', '4.317;2.580', '核心期刊;SA;JST;EI;CSCD');
INSERT INTO `search_journal` VALUES (2, '软件学报', 'http://www.jos.org.cn', '《软件学报》是一本刊登计算机软件各领域原创性研究成果的期刊,所刊登的论文均经过严格的同行专家评议.《软件学报》主要面向全球华人计算机软件学者,致力于创办与世界计算机科学和软件技术发展同步的以中文为主的\"中文国际软件学术期刊\",为全球华人同行提供学术交流平台.本刊不接受任何语种翻译稿.《软件学报》创刊于1990年,由中国科学院软件研究所和中国计算机学会联合主办.CN11-2560/TP, ISSN1000 -9825, CODEN RUXUEW.月刊,每期176面,每月6号出版.', '核心期刊;SA;JST;Pж(AJ);EI;CSCD', 'http://c61.cnki.net/CJFD/big/RJXB.jpg', 'Journal of Software', '中国科学院软件研究所', '4.259;2.658', '核心期刊;SA;JST;Pж(AJ);EI;CSCD');
INSERT INTO `search_journal` VALUES (3, '电子学报', 'http://www.jos.org.cn', '《电子学报》是中国电子学会主办的高级学术刊物,刊登电子与信息科学及相邻领域的原始（original）科研成果。1962年创刊，每月25日出版。本刊的办刊宗旨是反映中国电子与信息科学领域内的新理论、新思想、新技术，具有国内外先进水平的最新研究成果和技术进展，为促进国内外学术交流，促进中国电子与信息科学技术的快速发展服务。本刊设有：学术论文，科研通信，综述评论等栏目。凡以电子与信息科学为主体（交叉学科论文必须侧重电子与信息领域），在理论与应用实践上具有创新的，代表我国研究水平的学术论文，有科学依据和可靠数据的技术报告，阶段性成果报告，以及属于前沿学科，并对学科发展有指导意义的展望评论性文稿，均可向本刊投稿。由于本刊覆盖的学科专业较广，出版时有意识地将相关学科和专业集中：第1、4、7、10期主要是通信与信号处理；第2、5、8、11期主要是微电子学、计算机科学及相邻学科；第3、6、9、 12期主要是电子物理、真空电子学、微波与电磁场及相邻学科。', '核心期刊;CA;SA;JST;EI;CSCD', 'http://c61.cnki.net/CJFD/big/DZXU/DZXU201803.jpg', 'Acta Electronica Sinica', '中国电子学会', '1.520;1.115', '核心期刊;CA;SA;JST;EI;CSCD');
INSERT INTO `search_journal` VALUES (4, '计算机科学', 'http://www.jsjkx.com', '计算机科学》（月刊）创刊于1974年1月，由重庆西南信息有限公司（原科技部西南信息中心）主管主办，是中国计算机学会（CCF）会刊。主编陈国良，系中国科学院院士、全国首届高等学校国家教学名师。主要报道国内外计算机科学与技术的发展动态，涉及面广的方法论与技术和反映新苗头、能起承先启后作用的研究成果。《计算机科学》是中国科学引文数据库（CSCD）来源期刊、《中文核心期刊要目总览》（GCJC）收录期刊、中国科技核心期刊、中国期刊方阵双效期刊、RCCSE中国核心学术期刊、中文科技期刊数据库收录期刊、中国核心期刊（遴选）数据库收录期刊、中国学术期刊网络出版总库收录期刊，同时被美国剑桥科学文摘（CSA）、美国乌利希期刊指南（UPD）、日本科学技术振兴机构数据库（JST）收录。', '核心期刊;JST;CSCD', 'http://c61.cnki.net/CJFD/big/JSJA.jpg', 'Computer Science', '重庆西南信息有限公司', '1.087;0.669', '核心期刊;JST;CSCD');
INSERT INTO `search_journal` VALUES (5, '传感技术学报', 'http://j.chinatransducers.com', '《传感技术学报》创刊于１９８８年，是由国家教育部主管、中国微米纳米技术学会和东南大学联合主办发行的大１６K学术性月刊，她是我国在介绍传感器理论和应用领域方面较为全面的惟一的学术性刊物，是中国科技核心期刊，中文核心期刊。\r\n《传感技术学报》按栏目分:力学敏感器件、光学敏感器件、光纤敏感器件、生物、化学敏感器件、温度敏感器件、声学敏感器件、电磁学敏感器件、气体敏感器件、湿度敏感器件、机器人敏感器件、多种传感器技术处理的方法和理论、工艺技术、纳米材料及电子技术在传感器方面的应用等，同时也刊登具有国内外先进水平的最新研究成果。', '核心期刊;CA;SA;JST;CSCD', 'http://c61.cnki.net/CJFD/big/CGJS.jpg', 'Chinese Journal of Sensors and Actuators', '中国微米纳米技术学会;东南大学', '1.683;1.291', '核心期刊;CA;SA;JST;CSCD');
INSERT INTO `search_journal` VALUES (6, '自动化学报', 'http://www.aas.net.cn', '《自动化学报》（ACTA AUTOMATICA SINICA）是由中国自动化学会、中国科学院自动化研究所共同主办的高级学术期刊。本刊于1963年创刊，1966年停刊，1979年复刊，现为大16开本，月刊，每期160页。科学出版社出版，国内外公开发行。　《自动化学报》刊载自动化科学与技术领域的高水平理论性和应用性的科研成果，内容包括：1)自动控制；2)系统理论与系统工程；3)自动化工程技术与应用；4)自动化系统计算机辅助技术；5)机器人；6)人工智能与智能控制；7)模式识别与图像处理；8)信息处理与信息服务；9)基于网络的自动化等。学报编辑委员会由世界各地自动化领域的权威学者组成，编辑部设在中国科学院自动化研究所。', '核心期刊;SA;JST;EI;CSCD', 'http://c61.cnki.net/CJFD/big/MOTO.jpg', 'Acta Automatica Sinica', '中国自动化学会;中国科学院自动化所', '2.620;1.658', '核心期刊;SA;JST;EI;CSCD');
INSERT INTO `search_journal` VALUES (7, '浙江工业大学学报', 'http://xb.qks.zjut.edu.cn', '《浙江工业大学学报》是由浙江省教育厅主管、浙江工业大学主办的综合性学术刊物，1973年创刊，双月刊，国内外发行，国际标准刊号：ISSN 1006-4303，国内统一刊号：CN 33-1193/T，大16开本，每期120页。刊登学校各学科最新的研究成果，覆盖的学科主要有化工、材料、海洋、机械、信息、电子、生物、环境、药学、软件、建工、数学和物理等。获教育部科技发展中心“中国科技论文在线优秀期刊”一等奖，这是《浙江工业大学学报》继2014年首次获得二等奖后再次刷新历史纪录；入编北京大学《中文核心期刊要目总览》，连续被收录为中国科技核心期刊；被武汉大学中国科学评价研究中心第四届《中国学术期刊评价研究报告（武大版）（2015—2016）》评为“RCCSE中国核心学术期刊（A－）”。', '核心期刊;CA;SA;Pж(AJ)', 'http://c61.cnki.net/CJFD/big/ZJGD/ZJGD201803.jpg', 'Journal of Zhejiang University of Technology', '浙江工业大学', '0.891;0.645', '核心期刊;CA;SA;Pж(AJ)');
INSERT INTO `search_journal` VALUES (8, '计算机集成制造系统', 'http://www.cims-journal.cn', '《计算机集成制造系统》是中文月刊，外文名Computer Integrated Manufacturing Systems，期刊号ISSN l006-5911。   《计算机集成制造系统》1995年创刊。为国家863高技术研究发展计划CIMS主题公开出版的国家级学术刊物，由CIMS主题和中国兵器工业集团公司第210研究所共同主办。其宗旨是交流国内外CIMS研究、开发和应用的信息，推动和促进中国CIMS的发展。主要报道国内外有关发展计算机集成制造系统的政策措施、重点、趋势、科技成果、科研动态、推广应用、产品开发和学术活动等内容。设有综述、论文、专家论坛、企业实践和动态信息等栏目。”。', '核心期刊;SA;Pж(AJ);EI;CSCD', 'http://c61.cnki.net/CJFD/big/JSJJ.jpg', 'Computer Integrated Manufacturing Systems', '中国兵器工业集团第210研究所', '1.692;0.993', '核心期刊;SA;Pж(AJ);EI;CSCD');
INSERT INTO `search_journal` VALUES (9, '计算机工程与应用', 'http://cea.ceaj.org', '《计算机工程与应用》是由中国电子科技集团公司主管，华北计算技术研究所主办的面向计算机全行业的综合性学术刊物，系中国计算机学会会刊、计算机工程与应用学会学报，北大中文核心期刊、中国科技核心期刊、中国科学引文数据库(CSCD)来源期刊、《中国学术期刊综合评价数据库》来源期刊，收录在《中国期刊网》、《中国学术期刊(光盘版)》、英国《科学文摘》(SA/INSPEC)、俄罗斯《文摘杂志》(AJ)、美国《剑桥科学文摘》(CSA)、美国《乌利希期刊指南》、《日本科学技术振兴机构中国文献数据库》(JST)、波兰《哥白尼索引》(IC)，并荣获“中国期刊方阵双效期刊”、“中国精品科技期刊”、“工业和信息化部精品期刊”、“中国最具国际影响力学术期刊”、“中国百强科技期刊”、“期刊数字影响力100强”。', '核心期刊;SA;Pж(AJ);JST;CSCD', 'http://c61.cnki.net/CJFD/big/JSGG.jpg', 'Computer Engineering and Applications', '华北计算技术研究所', '1.692;0.993', '核心期刊;SA;Pж(AJ);JST;CSCD');
INSERT INTO `search_journal` VALUES (10, '仪器仪表学报', 'yqyb.etmchina.com', '《仪器仪表学报》是中国仪器仪表学会主办，代表中国仪器仪表及自动化最高学术水平的唯一国内外公开发行的学术性刊物。《仪器仪表学报》学术性强、内容创新、注重应用，优先刊登具有创新成就和观点的中英文论文、综述性文章、论坛及信息。', '核心期刊;CA;SA;JST;EI;CSCD', 'http://c61.cnki.net/CJFD/big/YQXB.jpg', 'Computer Engineering and Applications', '中国仪器仪表学会', '2.667;2.049', '核心期刊;CA;SA;JST;EI;CSCD');
INSERT INTO `search_journal` VALUES (11, '水力发电学报', 'http://www.slfdxb.com', '《水力发电学报》是中国水力发电工程学会主办的刊物，经中国科协批准为一级学术性刊物，1982年创刊定为季刊，2004年起改为双月刊，2015年起改为月刊，公开出版，国内外发行。本学报刊载与水力发电有关的科技学术论文，主要包括水力发电规划、水文水资源及水环境、水力学、泥沙工程学、潮汐和波浪发电、水工建筑物及水电站、工程建设管理、水轮机及其附属设备的运行与监测控制、水电站及水库群优化运行、水电工程与生态环境、水电工程监测等领域的研究性成果；及时反映各专业的科技成就、理论创新、经验总结及国内外学术动态，起到促进国内外学术交流的作用，在读者中享有良好的声誉。', '核心期刊;JST;CSCD', 'http://c61.cnki.net/CJFD/big/YQXB.jpg', 'Journal of Hydroelectric Engineering', '中国水力发电工程学会', '0.973;0.736', '核心期刊;JST;CSCD');
INSERT INTO `search_journal` VALUES (12, '模式识别与人工智能', 'http://manu46.magtech.com.cn/Jweb_prai', '《模式识别与人工智能》是由中国自动化学会、国家智能计算机研究开发中心和中国科学院合肥智能机械研究所共同主办、科学出版社出版的学术性期刊。本刊主要发表和报道模式识别、人工智能、智能系统等方面的研究成果与进展，旨在推动信息科学技术发展。\r\n本刊1989年创刊，月刊，主编为郑南宁院士。\r\n本刊创刊以来，得到较大发展，已成为模式识别、人工智能学术界有较大影响的刊物。', '核心期刊;JST;CSCD', 'http://c61.cnki.net/CJFD/big/MSSB/MSSB201802.jpg', 'Pattern Recognition and Artificial Intelligence', '中国自动化学会;国家智能计算机研究开发中心;中国科学院合肥智能机械研究所', '1.482;0.857', '核心期刊;JST;CSCD');
INSERT INTO `search_journal` VALUES (13, '计算机工程', 'http://www.ecice06.com', '《计算机工程》创刊于1975年，是中国电子科技集团公司第三十二研究所（华东计算技术研究所）和上海市计算机学会主办的学术性刊物，2013年起为月刊，每月15日出版。办刊宗旨： 贯彻党的“双百”方针，繁荣科技创作，促进国内外学术交流，探讨和传播计算机科学的理论和实践，加速和促进我国计算机事业的发展。本刊特点：以最快的速度、科学求实的精神，精选刊登代表计算机行业前沿科研、技术、工程方面的高、精、尖优秀论文。', '核心期刊;CA;SA;JST;Pж(AJ);CSCD', 'http://c61.cnki.net/CJFD/big/JSJC.jpg', 'Pattern Recognition and Artificial Intelligence', '华东计算机技术研究所;上海计算机学会', '0.901;0.550', '核心期刊;CA;SA;JST;Pж(AJ);CSCD');

SET FOREIGN_KEY_CHECKS = 1;
