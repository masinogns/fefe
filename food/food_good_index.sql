-- MySQL dump 10.13  Distrib 5.7.17, for osx10.12 (x86_64)
--
-- Host: localhost    Database: testdb
-- ------------------------------------------------------
-- Server version	5.7.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `food_good_index`
--

DROP TABLE IF EXISTS `food_good_index`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `food_good_index` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `area` varchar(50) DEFAULT NULL,
  `description` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food_good_index`
--

LOCK TABLES `food_good_index` WRITE;
/*!40000 ALTER TABLE `food_good_index` DISABLE KEYS */;
INSERT INTO `food_good_index` VALUES (1,'안산 대부도 방아머리 음식지구','방아머리는 경기도 안산시 대부동 방아머리 일대에 위치하며 대부도 초입에 있는 포구로 디딜방아의 방아머리처럼 생겼다하여 붙은 이름이다. 인근 바다에서 잡아 올린 싱싱한 해산물로 만든 바지락칼국수, 조개구이, 활어회 등 향토음식을 맛볼 수 있다. 서해 노을의 진수를 볼 수 있는 경관과 함께 바다의 정취와 사람 사는 냄새를 동시에 느낄 수 있는 곳이다.'),(2,'안산 댕이골','경기도 안산시 상록구 사동 1347 ~ 1352번지 일대 사동 야산 기슭에 자리 잡은 댕이골은 처녀의 댕기모양을 하고 있다 해서 붙여진 이름이다. 20여년 전 부터 한국 전통음식을 주 메뉴로 하는 음식점 들이 모이면서 먹거리 마을이 형성되었으며 육류는 물론 해물, 두부요리, 한정식, 채식에 이르기까지 입맛이 까다로운 사람도 즐길 수 있는 다양한 종류의 전통 먹을거리를 만날 수 있다.'),(3,'부산광역시 명륜1번가','부산광역시 동래구 명륜동에 소재하는 명륜1번가는 동래읍성, 복산동 고분군 등 역사적 상징성이 있고 지역 상권의 중심지로 부상하는 부산의 대표 먹거리 명소로 “청춘의 거리”, “젊음의 거리“, 장년의 거리”로 테마화된 먹거리타운 조성으로 청장년 누구나 부담 없이 이용할 수 있는 즐거움과 행복이 머무는 곳입니다.'),(4,'대구광역시 수성구 들안길','수성못 아래 넓은 들의 안쪽이라 하여 예로부터 \'수성 들안길\'로 불리는 음식지구로 대구시 수성구 상동, 두산동 일원에 위치하며 도로 양쪽으로 한식, 일식, 약식. 중식 등 전문음식점 150여개소가 밀집해 있어 대구 최고의 전문음식가로 자리잡았고, 인근에 수성유원지가 있어 식사 후 산책이나 휴식을 취하기에도 좋아 맛과 친절은 물론 자연친화적인 먹거리 타운으로 각광받고 있습니다.'),(5,'대구광역시 달서구 수밭골 웰빙음식거리',' \"대구광역시 달서구 수밭길(도원동) 일대에 위치하며 수밭골은 예로부터 숲이 많이 우거진 곳이라 하여 ‘숲밭골’이라 불리는데서 유래되었으며 지구 내 음식점은 ‘웰빙음식거리’라는 이름에 걸맞게 친환경'),(6,'강원도 평창군 오대산 산채마을','천년 고찰의 역사와 숨결이 있는 오대산 자락인 강원도 평창군 진부면 간평리, 동산리 일원에 위치하고 있어 사계절이 아름다운 이곳은 한 상 가득 25가지 이상의 신선한 산나물이 밑반찬으로 제공되는 산채정식이 유명한 곳으로 걷고 먹는 것 만으로도 자연이 주는 힐링을 마음껏 누릴 수 있는 곳이다.'),(7,'강원도 봉평 효석문화메밀마을','가산 이효석 선생님의 ‘메밀꽃 필 무렵’ 소설의 주요 배경인 강원도 평창군 봉평면 창동리, 원길리 일원에 위치하고 있으며 해마다 효석 문화제가 개최되는 곳으로 달빛처럼 하얀 메밀꽃이 아름다운 곳이며 주요 특산물인 메밀로 건강과 맛의 멋스러움을 온몸으로 느끼게 하는 메밀이야기를 먹을 수 있는 곳이다.'),(8,'경상남도 함양군 건강100세 음식지구','지리산과 덕유산 자락의 경남 함양군 삼양읍 상림공원 일원에 위치하며 천혜의 게르마늄이 풍부한 토양에서 생산된 함양 지역 농특산물을 이용한 차별화된 음식으로 관광객들에게 100세까지 건강하게 살 수 있도록 건강 음식을 제공한다.'),(9,'제주도 제주시 어영마을','제주시 용담2동 일원에 위치하며 제주국제공항과 가까워 관광객들이 많이 들려가는 곳이다. 제주를 대표하는 향토음식부터 회, 오리고기, 갈비, 양식 등 다양성 있는 맛집들은 물론이고, 맛있는 음식을 먹고 난 후 향긋한 커피에 취해볼 수 있는 카페에서 황금빛 찬란한 노을을 즐길 수 있는 제주도의 첫 관문이다.'),(10,'전라북도 전주시 한옥마을','전주 한옥 마을은 일제강점기인 1930년대 일본인들의 세력이 확장될 무렵, 당시 교동과 풍남문 일대에 거주하던 한국인들이일본에 대한 대립의식으로 한옥촌을 형성하면서 시작됐다.'),(11,'전라북도 고창군 선운산 풍천장어마을','풍천은 바닷물과 강물이 합쳐지는 지형으로서 선운사 어귀의 주진천(인천강)은 예부터 바닷물과 민물이 만나며 황토의 질이 가장 우수하고 황토에 함유되어 있는 영양염류가 매우 풍부하여 이곳에서 잡히는 풍천장어는 예로부터 타의 추종을 불허한다. 인천강이 흐르는 선운산 도립공원 초입인 전북 고창군 아산면 삼인리 일원에는 풍천장어 음식점 40개가 밀집되어 성업중이다.'),(12,'제주도 서귀포시 아랑조을 음식거리','서귀포시 천지동 중안로 서쪽 이면 도로를 중심으로 1번가, 2번가로 조성되어 있으며 제주도에서 맛볼 수 있는 특별한 특산 요리들과 함께 다양한 요리들을 드시고 갈 수 있는 거리로 세계적인 관광명소인 제주도를 대표하는 깨끗하면서 즐거운 먹거리가 가득한 문화공간입니다.');
/*!40000 ALTER TABLE `food_good_index` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-05-10  0:57:44
