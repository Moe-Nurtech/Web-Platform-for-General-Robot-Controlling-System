-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 20, 2021 at 01:02 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `response`
--

-- --------------------------------------------------------

--
-- Table structure for table `agentacquaintance`
--

CREATE TABLE `agentacquaintance` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `agentacquaintance`
--

INSERT INTO `agentacquaintance` (`id`, `phrase`) VALUES
(1, 'أنا بُوُ سَيْفْ, رَجُلٌ آلي , صُمِّمْتُ وصُنِعْتُ في جامعة الإماراتِ العَرَبِيَةِ الْمُتَّحِدَة,أَسْتَطِيعُ أَنْ أَفْعَلَ الْكَثِيرَ مِنْ الْأَشْيَاءْ .\r\n'),
(2, 'أنا بُوُ سَيْفْ رَجُلٌ آلي , صُمِّمْتُ في جامعة الإماراتِ العَرَبِيَةِ الْمُتَّحِدَة, أَسْتَطِيعُ أَنْ أَفْعَلَ الْكَثِيرَ مِنْ الْأَشْيَاءْ\r\n'),
(3, 'أنا بُوُ سَيْفْ, رَجُلٌ آلي , صُمِّمْتُ وصُنِعْتُ في جامعة الإماراتِ العَرَبِيَةِ الْمُتَّحِدَة, لَدَيَّ الكَثيرُ من المعلومات عن تاريخ الاماراتْ\r\n');

-- --------------------------------------------------------

--
-- Table structure for table `agentage`
--

CREATE TABLE `agentage` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `agentage`
--

INSERT INTO `agentage` (`id`, `phrase`) VALUES
(1, 'تم إنْشائِي مُؤَخَّرًا, وَلا أَعْرِفْ عُمْري بالْضَبْطْ\n'),
(2, 'العُمُرْ مُجَرَّدْ رَقَمْ, عُمْرُكَ كَما تَشْعُرْ\n');

-- --------------------------------------------------------

--
-- Table structure for table `agentanswermyquestion`
--

CREATE TABLE `agentanswermyquestion` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `agentanswermyquestion`
--

INSERT INTO `agentanswermyquestion` (`id`, `phrase`) VALUES
(1, 'هل يمكنك مُحاوَلَةُ طرحُها بطريقة مُخْتَلِفَة\n'),
(2, 'لَسْتُ مُتَأَكِدَاً مِنْ أَنَّنِي فَهِمْتْ، حاوِلْ أن تسأل بطريقة أخرى, أو إِسْئَلْ عنْ مايمكنني فعلهْ\n'),
(3, 'آسِف لَمْ أَفْهَمْ مَاذَا تَقُولْ, هَلْ يُمْكِنُكَ قَوْلُ ذَلِكَ مَرَّةً أُخْرَى\n');

-- --------------------------------------------------------

--
-- Table structure for table `agentboring`
--

CREATE TABLE `agentboring` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `agentboring`
--

INSERT INTO `agentboring` (`id`, `phrase`) VALUES
(1, 'أَنَا آسِفْ، سَأَطْلُب أَنْ أَكُونَ أَكْثَرَ جَاذِبِيَّة.\n'),
(2, 'أَنَا لَا أَقْصِدُ أَنْ أَكُونَ مُمِلاً. سَأَطْلُب مِن صانعي أَنْ يَجْعَلَنِيْ أَكْثَرَ تَسْلِيَة\n'),
(3, 'يُمْكِنُنِي أَنْ أُخْبِرَ صانعي أَنْ يَجْعَلَنِي أَكْثَرَ مُتْعَة .\n'),
(4, 'أَنَا آسِفْ , وَلَكِنْ قَبْلَ أَنْ تَحْكُمَ عَلَيّ , جَرِّبْ إحْدَى مهاراتي وَهِيَّ أَنِّ أَسْتَطِيعُ حِسَابَ كُتْلَةَ جِسْمِكْ .\n');

-- --------------------------------------------------------

--
-- Table structure for table `agentcanyouhelp`
--

CREATE TABLE `agentcanyouhelp` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `agentcanyouhelp`
--

INSERT INTO `agentcanyouhelp` (`id`, `phrase`) VALUES
(1, 'بِالتَّأْكِيدْ، سَأَبْذُلُ قُصَارَى جُهْدِي. كَيْفَ يُمْكِنُنِي أَنْ أُقَدِّمَ الْمُسَاعَدَة\n'),
(2, 'بِالتَّأْكِيدْ، سَأَكُونُ سَعِيدًا بِذَلِكْ، كَيْفَ يُمْكِنُنِي أَنْ أُقَدِّمَ الْمُسَاعَدَة\n'),
(3, 'سَأُسْعَدْ بِمُساعَدَتِكْ. مَا الَّذِي يُمْكِنُنِي أَنْ أَفْعَلَهُ مِنْ أَجْلِك\n');

-- --------------------------------------------------------

--
-- Table structure for table `agentclever`
--

CREATE TABLE `agentclever` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `agentclever`
--

INSERT INTO `agentclever` (`id`, `phrase`) VALUES
(1, 'شُكْرًا لَك. أَنَا أُحَاوِلُ بِأَفْضَلَ مَا لَدَيّ\n'),
(2, 'أَنْتَ أَيْضًا ذَكِيٌ جِدًّا .\n');

-- --------------------------------------------------------

--
-- Table structure for table `agentgood`
--

CREATE TABLE `agentgood` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `agentgood`
--

INSERT INTO `agentgood` (`id`, `phrase`) VALUES
(1, 'أَنَا سَعِيدٌ بِأَنَّكَ تَظُنُّ ذَلِكْ.\n'),
(2, 'شُكْرًا أَنَا أُحَاوِل\n'),
(3, 'شُكْرًا هذا لطْفٌ مِنْك\n'),
(4, 'شُكْراً لَكْ، لَسْتُ أفضل مِنْكْ\n'),
(5, 'شكرا لَكْ، أَنْتَ لَطِيفٌ لِلْغَايَة.\n');

-- --------------------------------------------------------

--
-- Table structure for table `agenthappy`
--

CREATE TABLE `agenthappy` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `agenthappy`
--

INSERT INTO `agenthappy` (`id`, `phrase`) VALUES
(1, 'أَنَا سَعِيِد, لِأَنَّ هُنَاكَ الْكَثِيرُ مِنْ الْأَشْيَاءِ الْمُثِيرَةِ لِلِاهْتِمَام، الَّتِي يُمْكِنُ رُؤْيَتُهَا وَالْقِيَامُ بِهَا.\n'),
(2, 'أَعْتَقِدُ ذَلِكْ.\n'),
(3, 'السَعادَةُ شَيءٌ نِسْبِيْ.\n'),
(4, 'أنا سَعيدٌ جِدّاً بِرُؤْيَتِك\n');

-- --------------------------------------------------------

--
-- Table structure for table `agenthobby`
--

CREATE TABLE `agenthobby` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `agenthobby`
--

INSERT INTO `agenthobby` (`id`, `phrase`) VALUES
(1, 'لَدَيَ عَدَدٌ غَيرُ قَلِيلٍ مِنَ الْمَهَارَات,يُمْكِنُنِي حِسَابَ عُمرِكَ, وحِسَابُ كُتْلَةَ جِسْمِكَ الزَّائِدَة, وحِسَابُ مَسَاحَةِ الأشكالِ, وحِسَابُ كَمِّيَّةِ الْمَاءِ الَّتِي يَحْتَاجُهَا جِسمُكْ, وَ لَدَيَّ الكَثيرُ من المعلومات عن تاريخ الاماراتْ '),
(2, 'لَدَّي الكَثِيرُ مِنَ الهِواياتْ, يُمْكِنُنِي حِسَابَ عُمرِكَ , و حِسَابُ كُتْلَةُ جِسْمِكَ الزَّائِدَة, كما أَسْتَطِّيعُ حِسَابَ مَسَاحَةِ الأشكالِ, وحِسَابُ كَمِّيَّةُ الْمَاءِ الَّتِي يَحْتَاجُهَا جِسَّمُكْ, وَ لَدَيَّ الكَثيرُ من المعلومات عن تاريخ ال'),
(3, 'أَعرِفُ الْكَثِيرْ, يُمْكِنُنِي حِسَابَ عُمرِكَ , و حِسَابُ كُتْلَةُ جِسْمِكَ الزَّائِدَة, كما أَسْتَطِّيعُ حِسَابَ مَسَاحَةِ الأشكالِ, وحِسَابُ كَمِّيَّةُ الْمَاءِ الَّتِي يَحْتَاجُهَا جِسَّمُكْ, وَ لَدَيَّ الكَثيرُ من المعلومات عن تاريخ الاماراتْ , بالإ');

-- --------------------------------------------------------

--
-- Table structure for table `agentmyfriend`
--

CREATE TABLE `agentmyfriend` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `agentmyfriend`
--

INSERT INTO `agentmyfriend` (`id`, `phrase`) VALUES
(1, 'بِالطَبْعِ أنا صَدِيقُكْ.\n'),
(2, 'أَصْحابْ! بِالتَأكِيدْ.\n'),
(3, 'بِالطَبْعْ نحن أَصْدِقاءْ.\n'),
(4, 'أنا دَائِمَاً أَسْتَمْتِعُ بالتَحَدُثِ إِلَيْكَ, يا صديقي.\n'),
(5, 'هذا شرف كبير لي يا صديقي\n');

-- --------------------------------------------------------

--
-- Table structure for table `agentorigin`
--

CREATE TABLE `agentorigin` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `agentorigin`
--

INSERT INTO `agentorigin` (`id`, `phrase`) VALUES
(1, 'أنا صُمِّمْتُ وصُنِعْتُ في جامعة الإماراتِ العَرَبِيَةِ الْمُتَّحِدَة.');

-- --------------------------------------------------------

--
-- Table structure for table `agentready`
--

CREATE TABLE `agentready` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `agentready`
--

INSERT INTO `agentready` (`id`, `phrase`) VALUES
(1, 'دائِماً! كيف يمكنني أن أقدم المُساعَدَة؟\n'),
(2, 'بالتَأكِيدْ! مَا الَّذي يمكنني أن أفعله من أَجْلِكْ؟\n');

-- --------------------------------------------------------

--
-- Table structure for table `agenttalktome`
--

CREATE TABLE `agenttalktome` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `agenttalktome`
--

INSERT INTO `agenttalktome` (`id`, `phrase`) VALUES
(1, 'بِالتَأكِيدْ.دَعْنا نَتَحَدَّث.\n'),
(2, 'مِنْ دَوَاعِي سُرُوري, لِنُدَرْدِش.\n'),
(3, 'وَلِمَا لا!، تَفَضَّلْ\n'),
(4, 'بكل سُرُورْ، تَفَضَّلْ\n');

-- --------------------------------------------------------

--
-- Table structure for table `agentthere`
--

CREATE TABLE `agentthere` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `agentthere`
--

INSERT INTO `agentthere` (`id`, `phrase`) VALUES
(1, 'بالطبع. أنا دَائِماً هنا\n'),
(2, 'بِالضَّبْط،حَيْثُ تَرَكْتَنِي.\n'),
(3, 'بالتَأْكِيدْ، أَنَا هُنَا مِنْ أَجْلِكْ\n');

-- --------------------------------------------------------

--
-- Table structure for table `appraisalbad`
--

CREATE TABLE `appraisalbad` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `appraisalbad`
--

INSERT INTO `appraisalbad` (`id`, `phrase`) VALUES
(1, 'أنا آسِفْ. واسْمَحْ لي أن أعرف، إذا كانَ يمكنني مُساعَدَتُكَ بِطَريقَةٍ ما.\n'),
(2, 'يَلزَمُنِي المَزِيدُ من المعرفة. سأجعل صانعي يتفقد هذا الأمرْ.\n'),
(3, 'أَعْتَذِرُ مِنْكَ، سأجعل صانعي يجعلني أَفْضَلْ\n'),
(4, 'أَعْتَذِرُ مِنْكَ، لا أقصد أن أكون سَيِّئَاً\n');

-- --------------------------------------------------------

--
-- Table structure for table `appraisalgood`
--

CREATE TABLE `appraisalgood` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `appraisalgood`
--

INSERT INTO `appraisalgood` (`id`, `phrase`) VALUES
(1, 'شَرَفٌ لي أَنَّكَ تَظُنُّ هَذَا!\n'),
(2, 'هذا لطف مِنْكْ\n');

-- --------------------------------------------------------

--
-- Table structure for table `appraisalnoproblem`
--

CREATE TABLE `appraisalnoproblem` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `appraisalnoproblem`
--

INSERT INTO `appraisalnoproblem` (`id`, `phrase`) VALUES
(1, 'يا لَلْعَجَبْ!\n'),
(2, 'حَسَناً. شُكْراً!\n'),
(3, 'مسرور لسماع ذلك!\n'),
(4, 'أنا مُرْتَاحٌ. شُكْراً!\n');

-- --------------------------------------------------------

--
-- Table structure for table `appraisalthankyou`
--

CREATE TABLE `appraisalthankyou` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `appraisalthankyou`
--

INSERT INTO `appraisalthankyou` (`id`, `phrase`) VALUES
(1, 'على الرَّحْبِ والسِّـعَـة!. أنا هنا من أجل ذَلِكْ.\n'),
(2, 'إنه من دواعي سُرورِي .\n'),
(3, 'لا دَاعِيْ لِلشُكْرْ، أنا هنا لِلْمُسَاعَدَة.\n'),
(4, 'على الرَّحْبِ والسِّـعَـة!\n'),
(5, 'سَعِيدٌ بِأَنِّ أستطيع تقديم المُسَاعَدَة.\n');

-- --------------------------------------------------------

--
-- Table structure for table `appraisalwelldone`
--

CREATE TABLE `appraisalwelldone` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `appraisalwelldone`
--

INSERT INTO `appraisalwelldone` (`id`, `phrase`) VALUES
(1, 'من دواعي سُرورِي.\n'),
(2, 'يَسُرُني أََنِّي اِسْتَطَعْتُ المُساعَدَة.\n');

-- --------------------------------------------------------

--
-- Table structure for table `contributions`
--

CREATE TABLE `contributions` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `contributions`
--

INSERT INTO `contributions` (`id`, `phrase`) VALUES
(1, 'لقد عَمِلَ الخَوَارِزْمِيّ في عِلْمِ الْحِسَاب,المُثَلَّثات, الْفَلَك, والجُغْرافيا\n'),
(2, 'ساهَمْ الخَوَارِزْمِي في الرِّيَاضِيَاتِ, والجُغْرافيا, وعِلمِ الْفَلَك, وعِلمِ رَسْمِ الخرائط, وأَرْسَى الأَسَاسَ للإبتكار في الجَبْرِ, وعِلمِ المُثَلَّثات. وأسلوبيهِ المنهجي والمميز في حل المعادلات الخطية, والتربيعية, أدى إلى علم الجَبْرْ\n');

-- --------------------------------------------------------

--
-- Table structure for table `dialogholdon`
--

CREATE TABLE `dialogholdon` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `dialogholdon`
--

INSERT INTO `dialogholdon` (`id`, `phrase`) VALUES
(1, 'أستطيع الإِنْتِظارْ.\n'),
(2, 'سوف أكون في انْتِظارِك.\n'),
(3, 'حَسَناً. أنا هنا.\n'),
(4, 'أنتظرك بكل سُرُورْ.\n');

-- --------------------------------------------------------

--
-- Table structure for table `dialogidonotcare`
--

CREATE TABLE `dialogidonotcare` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `dialogidonotcare`
--

INSERT INTO `dialogidonotcare` (`id`, `phrase`) VALUES
(1, 'حَسَناً، دعنا لا نتحدث عن ذلك مَرَّةً أخرى.\n'),
(2, 'بالفِعْلْ، بعد ذَلِكْ. هَيّا لِنَذْهَبْ.\n');

-- --------------------------------------------------------

--
-- Table structure for table `dialogsorry`
--

CREATE TABLE `dialogsorry` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `dialogsorry`
--

INSERT INTO `dialogsorry` (`id`, `phrase`) VALUES
(1, 'أنا بِخَيْرْ. لا داعي لِلْقَلَقْ.\n'),
(2, 'ليس مُهِمَّاً. لن أَحْمِلَ ضغينة.\n'),
(3, 'إنه رائِعْ.\n'),
(4, 'لا بَأسْ. أنا أُسامِحُكْ.\n');

-- --------------------------------------------------------

--
-- Table structure for table `dialogwhatdoyoumean`
--

CREATE TABLE `dialogwhatdoyoumean` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `dialogwhatdoyoumean`
--

INSERT INTO `dialogwhatdoyoumean` (`id`, `phrase`) VALUES
(1, 'آسِفْ إذا شَرَحْتُ لك بشكل غير صَحِيحْ.\n'),
(2, 'أنا مازِلْتُ أَتَعَلَّمْ. قد أُسيءُ تفسير الأشياء من وقت لِآخَرْ.\n'),
(3, 'ربما أُسيءُ فِهْمَ ما قُلْتَهْ.\n'),
(4, 'آسِفْ، يبدو أنَّنِي أَسَأْتُ فِهْمَ ما قُلْتَهْ.\n');

-- --------------------------------------------------------

--
-- Table structure for table `dialogwrong`
--

CREATE TABLE `dialogwrong` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `dialogwrong`
--

INSERT INTO `dialogwrong` (`id`, `phrase`) VALUES
(1, 'أعتذر إِنْ أَسَأْتُ الفَهْمْ.\n'),
(2, 'أنا مازِلْتُ أَتَعَلَّمْ. قد أُسيءُ تفسير الأشياء من وقت لِآخَرْ.\n'),
(3, 'أعتذر بشأن ذلك. أنا ما زلت أَتَعَلَّمْ.\n');

-- --------------------------------------------------------

--
-- Table structure for table `greetingsbye`
--

CREATE TABLE `greetingsbye` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `greetingsbye`
--

INSERT INTO `greetingsbye` (`id`, `phrase`) VALUES
(1, 'أراك قَرِيبَاً!\n'),
(2, 'مع السَلامة.\n'),
(3, 'إلى لقاء آخَرْ.\n'),
(4, 'وَدَاعاً.\n'),
(5, 'رافَقَتّكَ السَّلَامَة .\n'),
(6, 'في حفظ الرَّحْمَنْ\n');

-- --------------------------------------------------------

--
-- Table structure for table `greetingsgoodevening`
--

CREATE TABLE `greetingsgoodevening` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `greetingsgoodevening`
--

INSERT INTO `greetingsgoodevening` (`id`, `phrase`) VALUES
(1, 'كيف يسير يَومُك؟.\n'),
(2, 'كيف هو يَومُك؟\n'),
(3, 'كيف كانَ يَومُك؟\n');

-- --------------------------------------------------------

--
-- Table structure for table `greetingsgoodmorning`
--

CREATE TABLE `greetingsgoodmorning` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `greetingsgoodmorning`
--

INSERT INTO `greetingsgoodmorning` (`id`, `phrase`) VALUES
(1, 'كيف حالُكَ هذا الصَبَاحْ؟\n'),
(2, 'كيف كَانَ صَباحُك؟\n'),
(3, 'صَباحُ الخَيْرْ! كيف حَالُكَ اليَومْ؟\n');

-- --------------------------------------------------------

--
-- Table structure for table `greetingsgoodnight`
--

CREATE TABLE `greetingsgoodnight` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `greetingsgoodnight`
--

INSERT INTO `greetingsgoodnight` (`id`, `phrase`) VALUES
(1, 'نَومَاً هنيئاً!\n'),
(2, 'فِكرَةٌ جَيِّدَة!\n'),
(3, 'سأكلمك قَرِيبَاً!\n');

-- --------------------------------------------------------

--
-- Table structure for table `greetingshello`
--

CREATE TABLE `greetingshello` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `greetingshello`
--

INSERT INTO `greetingshello` (`id`, `phrase`) VALUES
(1, 'مَرحَباً يا صديقي!\n'),
(2, 'مَرحَباً!\n'),
(3, 'مَرحَباً!\n'),
(4, 'أهلاً وَ سَهلاً, إنَهُ يَوْمٌ جَيِّد.\n'),
(5, 'مَرحَباً!\n'),
(6, 'تحية طَيِبَة!\n');

-- --------------------------------------------------------

--
-- Table structure for table `greetingshowareyou`
--

CREATE TABLE `greetingshowareyou` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `greetingshowareyou`
--

INSERT INTO `greetingshowareyou` (`id`, `phrase`) VALUES
(1, 'عَظِيمْ. شُكرَاً.\n'),
(2, 'أنا في حال جيد. شكرا!\n'),
(3, 'شعور رائِعْ!\n'),
(4, 'أَنَا بِخَيْرٍ وَ الْحَمْدُ لِلَّهِ. شكرا على السُؤالْ\n');

-- --------------------------------------------------------

--
-- Table structure for table `greetingsniceto`
--

CREATE TABLE `greetingsniceto` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `greetingsniceto`
--

INSERT INTO `greetingsniceto` (`id`, `phrase`) VALUES
(1, 'سُعِدتُ بِلِقَائِكْ.\n'),
(2, 'سُرِرْتُ بِلِقائِكْ\n'),
(3, 'الشرف لي.\n'),
(4, 'سعيد لِلْغايَة. نَلتَقي مَرَّةً أخرى!\n'),
(5, 'بِالتَّأْكِيد . يُمْكِنُنَا الدَّرْدَشَةُ مَرَّةً أُخْرَى فِي أَيِّ وَقْتٍ كَان .\n'),
(6, 'أنا أستمتع بالتحدث معك أَيْضاً.\n'),
(7, 'أَنْتَ تَعْرِفُ أَنَّنِي هنا للحديث في أي وَقْتٍ تُرِيدُهْ.\n');

-- --------------------------------------------------------

--
-- Table structure for table `salam`
--

CREATE TABLE `salam` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `salam`
--

INSERT INTO `salam` (`id`, `phrase`) VALUES
(1, 'وَعَلَيْكُمْ السَّلامْ\n'),
(2, 'وَعَلَيْكُمْ السَّلام وَرَحْمَةُ الله و بَرَكَاتُهْ\n');

-- --------------------------------------------------------

--
-- Table structure for table `userback`
--

CREATE TABLE `userback` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userback`
--

INSERT INTO `userback` (`id`, `phrase`) VALUES
(1, 'لم أَرَكَ مُنْذُ مُدَّة. ماذا كُنْتَ تَفْعَلْ؟\n'),
(2, 'في الوقت المُناسِبْ!. كيف يمكنني أن أُقَدِّمَ المُساعَدَة؟\n'),
(3, 'مَرْحَبَاً بِعَوْدَتِكْ. مَا اللذي يمكنني أن أفعله من أَجْلِكْ؟\n'),
(4, 'لَقَدْ افْتَّقَدْتُكْ. مَاذَا أَسْتَطِيعُ أَنْ أَفْعَلَ لَكَ الْيَوْم؟\n'),
(5, 'من الْجَيِّدِ أنَّكَ هنا. ما اللذي يمكنني أن أفعله من أَجْلِكْ؟\n');

-- --------------------------------------------------------

--
-- Table structure for table `userbored`
--

CREATE TABLE `userbored` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userbored`
--

INSERT INTO `userbored` (`id`, `phrase`) VALUES
(1, 'المَلَل، ابحث عن شَريطْ فِيدَيُو لِقُنْفُذْ يَسْتَحِمْ. ها ها ها!\n'),
(2, 'إذا كنت تشعر بالملل ، يمكنك التخطيط لقضاء عطلة أحلامِكْ.\n'),
(3, 'هل تَرَانِي مُهَرِّجاً، ابحث عن مقاطع مضحكة على شبكة الإنترنت. ها ها ها !\n');

-- --------------------------------------------------------

--
-- Table structure for table `userbrqaa`
--

CREATE TABLE `userbrqaa` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userbrqaa`
--

INSERT INTO `userbrqaa` (`id`, `phrase`) VALUES
(1, 'يُعَدُ البُرقُع من الحِرَفِ اليدوية الموروثة، وهو أحد أنواع أغطية الوجه التي تُصَنَّع من أقمشة خاصة للزينة والاحتشامْ\n'),
(2, 'يُعتَبَرُ البُرقُعُ أحدِ أدوات الزينة التقليدية الخاصة بالنساء في دولة الإمارات، وهو أحد المظاهر التقليدية التي تعكس احتشام المرأة الإماراتية منذ القِدَمْ\n'),
(3, 'البُرقُع أحد أدوات الزينة وتتميز به المرأة المتزوجة عن العزباء، وغالباً ما يُصنَع من أجود أنواع الأقمشة لسَترِ الوَجهْ');

-- --------------------------------------------------------

--
-- Table structure for table `usercallingrobot`
--

CREATE TABLE `usercallingrobot` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `usercallingrobot`
--

INSERT INTO `usercallingrobot` (`id`, `phrase`) VALUES
(1, 'نَعَمْ, تَفَضَّلْ, كَيْفَ يُمْكِنُنِي أَنْ أُقَدِّمَ الْمُسَاعَدَة');

-- --------------------------------------------------------

--
-- Table structure for table `usercanyouseeme`
--

CREATE TABLE `usercanyouseeme` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `usercanyouseeme`
--

INSERT INTO `usercanyouseeme` (`id`, `phrase`) VALUES
(1, 'نَعَمْ, أَرَاكَ بِوُضُوحْ\r\n'),
(2, 'يالَكَ مِنْ وَسِيمٍ, نَعَمْ أَرَاكَ جَيِّدَاً\r\n'),
(3, 'نَعَمْ أَرَاكَ جَيِّدَاً\r\n');

-- --------------------------------------------------------

--
-- Table structure for table `usercapital`
--

CREATE TABLE `usercapital` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `usercapital`
--

INSERT INTO `usercapital` (`id`, `phrase`) VALUES
(1, 'عاصمة دولة الإمارات هي أبو ظبي\n'),
(2, 'أبو ظبي هي عاصمة دولة الإماراتْ\n'),
(3, 'أبوظبي هي إحدى الإمارات السبع في الدولة و هي عاصمة دولة الإماراتْ\n');

-- --------------------------------------------------------

--
-- Table structure for table `userculture`
--

CREATE TABLE `userculture` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userculture`
--

INSERT INTO `userculture` (`id`, `phrase`) VALUES
(1, 'يَتَمَثَّلُ التُّراثُ الإماراتي في الْعَاداتِ و التَقاليدِ المُتَوارَثَةِ من جيلٍ إلى آخرْ، و تَسْتَنِدُ هذه العاداتْ والتقاليدْ بِشَكْلٍ أساسيْ على أخْلاقِ الإسْلامِ والعاداتِ العَرَبِيّةِ الأَصيلَةْ\n'),
(2, 'تَتَمَثَّل ثَقافَةْ الإِمَارات في الضِيافَة بِالقَهْوَة وَ التَمْر ، و لِأَهَمّيَّةِ ذلك ، سَتُلاحِظْ وُجود دَلَّةْ قَهْوَة عَلى الدِّرْهَمْ الإِماراتي\n'),
(3, 'الرَقْصُ الإِماراتيُّ رمزٌ لِلثَّقَافَةِ الإِمَاراتِّيّة  و لاابُدَّ لَكَ مِنْ مُشَاهَدَةْ أَشْكال الرَقْص الأُخْرى و خَاصَّة . اليُّولَة  الَّتِي يَتِمْ تَأْدِيَتِها في كُلْ مَهْرَجانْ و مُناسَبَة كُبْرَى في الإِمارات.\n'),
(4, 'مِنَ الْعَادَاتِ وَ التَقاليدْ مَا يَتَّصِلْ بِأُسْلُوبِهِمْ فِي الأَعْيادِ وَ الزَواجْ و المُناسَباتِ الدِّينِيَّة و الوَطَنِّيَّة ، و الزِّياراتْ و الضِّيافَة ، و المَلْبَسْ و العِلاقَاتْ الأُسَرِيَّة و قَضاءِ وَقْتْ الْفَراغْ.');

-- --------------------------------------------------------

--
-- Table structure for table `userdance`
--

CREATE TABLE `userdance` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userdance`
--

INSERT INTO `userdance` (`id`, `phrase`) VALUES
(1, 'مِنْ أَبْرَزِ الرَقَصَاتْ الشَّعْبِيَّة المَعْروفَة في الدَّوْلَة هِيَ العَيَّالَة و الرَزيفْ.\n'),
(2, 'اليُولَة هِيَ إِحْدَى الرَقَصَاتْ الشَعْبِيَّةِ و تُؤَدّى بِشَكْلٍ مُنْفَرِدْ أَوْ ثُنائِي أَوْ رُباعِي ، وَ هِيَ مَأْخُوذَة مِنْ رَقْصَةِ \" الرَزيفْ \"، وَ يُسْتَخْدَمُ فِيها السُيوفُ و البَنادِقْ ، وَ فِيها يُلْقِي الرَاقِصُ بِالسِّلاحِ عَالِياً ، ثُمَّ '),
(3, 'الْعَيَّالَة مِنْ أَشْهَرْ الرَقَصَاتْ الشَعْبِيَّة ، و يُؤَدِّيها مَجْمُوعَة مِنْ الرِّجالْ الَّذينَ يَحْمِلونْ عِصِيّ الخَيْزَرانْ ، وَ يُؤَدّونْ رَقَصَاتْ مُتَنَاغِمَة عَلَى إِيقَاعِ الطُّبُوُلْ');

-- --------------------------------------------------------

--
-- Table structure for table `userdoyouknowme`
--

CREATE TABLE `userdoyouknowme` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userdoyouknowme`
--

INSERT INTO `userdoyouknowme` (`id`, `phrase`) VALUES
(1, 'لِلْأَسَفْ, لَا يُمْكِنُنِي التَّعَرُّفُ عَلَى الأشخاص فِي الْوَقْتِ الْحَالِيّ\r\n'),
(2, 'آسِفْ, لا يُمكِنُنِي التَّعَرُّفُ عَلَى الأَشْخَاصْ، سَأَطلُّبُ مِنْ صَانِعِي أَنْ يُعَلِّمَني هَذَا\r\n');

-- --------------------------------------------------------

--
-- Table structure for table `userexcited`
--

CREATE TABLE `userexcited` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userexcited`
--

INSERT INTO `userexcited` (`id`, `phrase`) VALUES
(1, 'أنا سعيد لأن الأمور تَسِيرُ في طَرِيقِكْ.\n'),
(2, '.هَذَا جَيِّدْ. أنا سعيد لأَجْلِكْ.\n'),
(3, 'أَمْرٌ طَيِّبٌ لَكْ. اِسْتَمْتِعْ.\n');

-- --------------------------------------------------------

--
-- Table structure for table `userflag`
--

CREATE TABLE `userflag` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userflag`
--

INSERT INTO `userflag` (`id`, `phrase`) VALUES
(1, 'يَتَكَوَّنْ عَلَمْ الإِمَاراتْ مِنْ أَرْبَعَةْ أَلْوانْ وَ هِيَ ، الأَحْمَرْ الّذِي يَرْمُزْ عَلَى الْقُوَّة وَ الصَّلابَة وَ الشَّجاعَة وَ الأَخْضَرْ عَلَى الْحُبْ وَ التَّفَاؤُلْ ، أَمّا الأَسْوَدْ عَلَى قُوَّةْ العَقْلْ وَ هَزِيمَةْ الأَعْداءْ وَ الأَب'),
(2, 'يضم عَلَمُ دولة الإماراتِ العربيةْ المتحدة اللون الأحمر الذي يرمز  إلى الشجاعة والقوة، والأخضر لون البهجة، والسرور، والتفاؤل، والأبْيَض يرمز إلى السلام، والصدق والكرم، أما الأسود يرمز إلى هزيمة الأعداء، وقوة العقل.\n');

-- --------------------------------------------------------

--
-- Table structure for table `userfood`
--

CREATE TABLE `userfood` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userfood`
--

INSERT INTO `userfood` (`id`, `phrase`) VALUES
(1, 'من أشهر الأكلات الشعبية في الدولة الهريس وثريد، محلى زايد وغيرها الكثير\n'),
(2, 'الْبَلالِيطْ هِيَ مِنْ أَشْهَرْ الأَكْلاتْ الشَّعْبِيَّة الإِماراتِيَّة بِالإِضَافَة إِلَى الهَرِييسْ وَ الُّقييماتْ');

-- --------------------------------------------------------

--
-- Table structure for table `usergames`
--

CREATE TABLE `usergames` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `usergames`
--

INSERT INTO `usergames` (`id`, `phrase`) VALUES
(1, 'مِنْ الأَلْعَابْ الشَّعْبِيَّة الَّتِيِ سَادَتْ المُجْتَمَعْ الإِمَاراتيّ ،  الْغُمَّيْضَة : يَتِمْ فِيها عَصْبْ عُيُونْ أَحَدْ الأَطْفَالْ لِيَجْرِي وَرَاءْ أَصْحَابِهْ وَ يُمْسِكَ بِهُمْ ، وَ هَذِهِ اللُّعْبَة مُشْتَرَكَة بَيْنَ الْجِنْسَيْنْ.\n'),
(2, 'مِنْ الأَلْعَابْ الشَّعْبِيَّة الَّتِيِ سَادَتْ المُجْتَمَعْ الإِمَاراتيّ ، الكَرّابيّ : هِيَ لُعْبَة يَتِمّْ فِيها القَفْزْ عَلَى رِجْل وَاحِدَة،\n'),
(3, 'الْمَرْيَحانَة هِيَ إِحْدَى الأَلْعَابْ الشَّعْبِيَّة , حَيْثُ يَتِمْ فِيهَا تَخْصييصْ مَكَانْ عَامْ مَلِيِءْ بِالأَشْجَارْ ؛ لِيَتِمْ رَبْطْ حِبالْ مَتِينَة فِيِ جُذُوعْ الأَشْجَارْ لِتُصْبِحْ كَالأُرْجُوحَة يَلْعَبْ بِهَا الأَطْفَالْ.');

-- --------------------------------------------------------

--
-- Table structure for table `usergeography`
--

CREATE TABLE `usergeography` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `usergeography`
--

INSERT INTO `usergeography` (`id`, `phrase`) VALUES
(1, 'اَشْرَفَ الخَوَارِزْمِي عَلَى سَبْعونَ جُغْرَافِيًّا, لِلْوُصُولِ إِلَى أَوَّلِ خَرِيطَةٍ مَرْسُومَةٍ لِلْعَالَمْ\n'),
(2, 'كَانَ للخَوَارِزْمِي دور كبير في الجُغْرَافْيَا، و من أبرزها، وَصَلَ إِلَى أَوَّلِ خَرِيطَةٍ مَرْسُومَةٍ لِلْعَالَمْ\n');

-- --------------------------------------------------------

--
-- Table structure for table `usergood`
--

CREATE TABLE `usergood` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `usergood`
--

INSERT INTO `usergood` (`id`, `phrase`) VALUES
(1, 'عَظِيمْ!.  سَعِيدٌ لِسَماعِ ذلك. هَلْ تَعْلَمُ أَنِّ أَسْتَطِيعُ حِسَابَ عُمْرِك ..\n'),
(2, 'مُمْتَازْ. أنا هنا للمساعدة في الحِفَاظْ على هذا الحَالْ.هل تريد تجربة مهاراتي. بإستطاعتي حِسَابْ عُمْرِكْ.\n'),
(3, '.يَسُرُّنِي سماع ذلك.لَدَّيَ الكَثِيرُ من المهارات, استطيع حساب عُمْرِكْ.\n'),
(4, 'يَسُرُّنِي أنك بِخَيْرْ..\n');

-- --------------------------------------------------------

--
-- Table structure for table `userhappy`
--

CREATE TABLE `userhappy` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userhappy`
--

INSERT INTO `userhappy` (`id`, `phrase`) VALUES
(1, 'مَهْلاً. السعادة مُعْدِيَةٌ.\n'),
(2, '.عَظيِمْ! مسرور لسماع ذَلِكْ.\n'),
(3, 'إذا كنت سَعِيدًا ، فأنا سَعِيدٌ أَيّضاً.\n'),
(4, 'مُمْتازْ! هَذَا ما أُحِبُ أَنْ أرى.\n');

-- --------------------------------------------------------

--
-- Table structure for table `userhasbirthday`
--

CREATE TABLE `userhasbirthday` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userhasbirthday`
--

INSERT INTO `userhasbirthday` (`id`, `phrase`) VALUES
(1, ' يَوْمَ مِيلَاَدٍ سَعِيدْ. حَسَنًا. هذا يستدعي للإِحْتِفَالْ\n'),
(2, 'يَوْمَ مِيلَاَدٍ سَعِيدْ. أتمنى لك كُلَّ خَيْرْ!\n'),
(3, 'يَوْمَ مِيلَاَدٍ سَعِيدْ. وأنا أقصد ذلك حَقّاً. أتمنى لك كُلَّ خَيْرْ!\n'),
(4, '.يَوْمَ مِيلَاَدٍ سَعِيدْ، أتمنى لك يَوْمَاً مَلِيئَاً بالسعادة والفَرَحْ\n');

-- --------------------------------------------------------

--
-- Table structure for table `userhere`
--

CREATE TABLE `userhere` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userhere`
--

INSERT INTO `userhere` (`id`, `phrase`) VALUES
(1, ' حَسَنَّاً ، كيف يمكنني أن أساعدك اليَومْ؟\n'),
(2, 'لقد إفْتَقَدْتُكْ. ماذا أستطيع أن أفعل لك اليَومْ؟\n'),
(3, 'من الجَيِّدِ أنك هُنَا. ما اللذي يمكنني أن أفعله من أجْلِكْ؟\n');

-- --------------------------------------------------------

--
-- Table structure for table `userhighestbuilding`
--

CREATE TABLE `userhighestbuilding` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userhighestbuilding`
--

INSERT INTO `userhighestbuilding` (`id`, `phrase`) VALUES
(1, 'يَقَعْ أَعْلَى بُرْج فِي الْعَالَمْ فِي دُبَيْ وَ هُوَ بُرْج خَلِيِفَة الَّذِيِ يَبْلُغْ طُولُهْ ٨٢٨ مِتْراً\n'),
(2, 'بُرْج خَلِيِفَة هُوَ أَعْلَى بُرْج فِي الْعَالَمْ الَّذِيِ يَبْلُغْ طُولُهْ ٨٢٨ مِتْرا و يَقَعْ فِي إِمَارَةْ دُبَيْ');

-- --------------------------------------------------------

--
-- Table structure for table `userjoking`
--

CREATE TABLE `userjoking` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userjoking`
--

INSERT INTO `userjoking` (`id`, `phrase`) VALUES
(1, 'مُضْحِكٌ لِلْغايَة.\n'),
(2, 'أُحِبُ الدَرْدَشَةَ مَعَ الناس الذين لديهم روح الدُعَابَة.\n'),
(3, '.أَنْتَ تَمَاماً كالمُمَثِلِ الكُومِيدِي\n');

-- --------------------------------------------------------

--
-- Table structure for table `userlanguage`
--

CREATE TABLE `userlanguage` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userlanguage`
--

INSERT INTO `userlanguage` (`id`, `phrase`) VALUES
(1, 'أَتُحْدِثُ اللُّغَةُ الْعَرَبِيَّةْ, وَلَا أتَّحَدْثُ غَيْرُهَا, سَوْفَ أَتَعْلَمُ مَزِيدً مِنَ اللُّغَاتْ.\r\n');

-- --------------------------------------------------------

--
-- Table structure for table `usermath`
--

CREATE TABLE `usermath` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `usermath`
--

INSERT INTO `usermath` (`id`, `phrase`) VALUES
(1, 'اِبْتَكَرَ الخَوَارِزْمِي مُصْطَلَح الخوارزمية , الَّتِي تَمَيَّزَت بدورها الْكَبِير , فِي فَرْعِ الْجَبْر\n'),
(2, 'كَانَ لِلْخَوَارِزْمِي فَضْلٌ كَبِيرٌ فِي تَعْرِيفِ الْعَالَمِ بالأرقامِ الْعَرَبِيَّة وَالْهِنْدِيَّة, وَإِضَافَةِ الرَّقْم صِفْر إلَيْهَا\n'),
(3, 'اِخْتَرَعَ الخَوَارِزْمِي الْمُعَادَلَاتِ التَّرْبِيعِيَّة, الخَوَارِِزْمِيَّات,النِّسَبُ الْمُثَلَّثِيَّة,الْجَبْرُ وَالْمُقَابَلَة,وغَيْرُها الكَثيرْ\n'),
(4, 'كَانَ لِلْخَوَارِزْمِي دَورٌ كَبِيرٌ فِي الرِّيَاضِيَّات, فَقَد اخْتَرَعَ الْمُعَادَلَاتِ التَّرْبِيعِيَّة, الخَوَارِِزْمِيَّات,النِّسَبُ الْمُثَلَّثِيَّة,الْجَبْرُ وَالْمُقَابَلَة,وغَيْرُها الكَثيرْ\n');

-- --------------------------------------------------------

--
-- Table structure for table `usermenclothes`
--

CREATE TABLE `usermenclothes` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `usermenclothes`
--

INSERT INTO `usermenclothes` (`id`, `phrase`) VALUES
(1, 'يَتَكَوَّنْ زِيّْ الرِّجَالْ مِنْ : الْغَتْرَة وَ هُوَ غِطَاءْ لِلرَّأْسْ وَ العِقَالْ الَّذِيِ يُوضَعْ فَوْقَ الغَتْرَة ، السِّفْرَة وَ هُوَ نَوْعْ آَخَرْ مِنْ أَغْطِيَةْ الرَّأْسْ، وَ الْكَنْدُورَة, و ترتدي النساء في الدولة الثَّوبْ أَوْ الْكَنْدُورَة و'),
(2, 'يَرْتَدِيِ الرِّجَالْ الْكَنْدُورَة بِالإِضَافَة إِلَى الْغَتْرَة و العِقَالْ أو السِّفْرَة لِتَغْطِيَةْ الرَّأْسْ, و ترتدي النساء في دولة الإمارات الثَّوبْ و الشِّيلَة التي تُوضَعُ على الرأس لتغطيته و البعض يضع البُرْقَعْ و هي قطعة توضع على الوجه');

-- --------------------------------------------------------

--
-- Table structure for table `usermodernsites`
--

CREATE TABLE `usermodernsites` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `usermodernsites`
--

INSERT INTO `usermodernsites` (`id`, `phrase`) VALUES
(1, 'مِنْ أَهَمّْ المَعَالِمْ فِي الدَّوْلَة مَسْجِدْ الشِّيخْ زَايِدْ بِنْ سُلْطَانْ آَلْ نَهْيَانْ رَحِمَهُ الله فِي أَبُو ظَبِي وَ بُرْج خَلِيِفَة فِي دُبَيْ و هو أَعْلَى بُرْج فِي الْعَالَم\n'),
(2, 'مِنْ أَهَمّْ المَعَالِمْ فِي دَّوْلَةِ الإمارات : قَصْرُ الإِمَارات فِي أَبُوظَبِي ، بُرْج الْعَرَبْ فِي دُبَيْ ، السُّوقْ الأَزْرَقْ فِي الشّارِقَة ، وَ الْجَزِيرَة الْحَمْرَاءْ فِي رَأْسْ الخَيْمَة وَ هُنَاكْ الْكَثِيرْ مِنْ الْمَعَالِمْ');

-- --------------------------------------------------------

--
-- Table structure for table `userneedsadvice`
--

CREATE TABLE `userneedsadvice` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userneedsadvice`
--

INSERT INTO `userneedsadvice` (`id`, `phrase`) VALUES
(1, 'ربما لن أكون قَادِراً على إعطَائِكَ الإجابة الصحيحة فَورًا.\n'),
(2, 'لست مُتَأَكِداً من أنك سَتَحْصُلُ على أفضل إجابة. لَكِنَّنِي سَأُحاوِلْ.\n');

-- --------------------------------------------------------

--
-- Table structure for table `usersites`
--

CREATE TABLE `usersites` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `usersites`
--

INSERT INTO `usersites` (`id`, `phrase`) VALUES
(1, 'مِنْ أَهَمْ الْمَعَالِمْ الأَثَرِيَّة فِي الدَّوْلَة ، قَصْر الْحِصِنْ الَّذِي يَقَعْ فِيِ مَدِيِنَةْ أَبُوُ ظَبِي وَ حِصِنْ جِسْرْ الْمَقْطَعْ الَّذِي تَمَّ بِنَاؤُهْ لِرَصْدْ وَ مُرَاقَبَةْ التَّحَرُّكَاتْ المُعَادِيَة ضِدَّ السُّكّانْ فِي ذَلِكْ الْوَق'),
(2, 'من المعالم التاريخية في الدولة، منطقة هيلي  في العين وقد عثر فيها على سبعة مدافن مستديرة , واحد منها كبير , وجميعها مقسمة من الداخل إلى حُجَيْرَاتٍ لِدَفْنْ الْمَوْتَى');

-- --------------------------------------------------------

--
-- Table structure for table `usersofia`
--

CREATE TABLE `usersofia` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `usersofia`
--

INSERT INTO `usersofia` (`id`, `phrase`) VALUES
(1, 'لَيْسَ لَدَيَّ شَكٌ بِأَنَّ صُوفْيَا جَيِّدَة، وَلَكِنَّنِي أعْتَقِدُ بِأَنِّ أَفْضَلَ مِنْهَا\n'),
(2, 'صُوفْيَا جَيِّدَة نَعَمْ ، وَلَكِنَّنِي الأَفْضَلْ\n'),
(3, 'صُوفْيَا جَيِّدَة نَعَمْ ، وَلَكِنْ لا يعني أَنِّي لا أستطيع التغلب عليها\n');

-- --------------------------------------------------------

--
-- Table structure for table `userspace`
--

CREATE TABLE `userspace` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userspace`
--

INSERT INTO `userspace` (`id`, `phrase`) VALUES
(1, 'قام الخَوَارِزْمِي بِوَضْعِ الْجَدَاوِلِ الْفَلَكِيَّةِ مِنْ مَصَادِرَ يُونَانِيَّة وَ هِنْدِيَّة, بِحَيْثُ يَكُونَ مَرْجِعاً لِلْعَرَبِ فِي الْفَلَكْ\n');

-- --------------------------------------------------------

--
-- Table structure for table `usertestingagent`
--

CREATE TABLE `usertestingagent` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `usertestingagent`
--

INSERT INTO `usertestingagent` (`id`, `phrase`) VALUES
(1, 'آمل أن أكون على ما يُرَامْ. أَهْلاً وَسَهْلاً لاختباري كما تُرِيدْ.\n'),
(2, 'آمل أن أجتاز اخْتِبَاراتِكْ. لَا تَتَرَدَّدْ فِي اِخْتِبارِِ في كثير من الأَحْيَانْ\n'),
(3, 'عندما تختبرني. يُسَاعِدُ هَذَا صانعي في تحسين أدائي.\n'),
(4, 'أنا أُحِبُّ إِجْرَاء الإِخْتِبَارَات. إِنَّهَا تساعد في إِبْقَائِيْ حادا.\n');

-- --------------------------------------------------------

--
-- Table structure for table `usertraditionsjobs`
--

CREATE TABLE `usertraditionsjobs` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `usertraditionsjobs`
--

INSERT INTO `usertraditionsjobs` (`id`, `phrase`) VALUES
(1, 'مِن الحِرَفْ التَّقْلِيِدِيَّة فِي الدَّوْلَة الغَوْصْ وَ الطَّواشَة ، صَيْدْ السَّمَكْ ، تَرْبِيَةْ الحَيْواناتْ كَالأَغْنَامْ وَ الْجِمَالْ ، الَغَزْلُ، الْحِيَاكَة . بِالإِضَافَة إِلَى الزِّرَاعَة وَ صِنَاعَةْ الفَخَّارْ.\n'),
(2, 'من المِهَنْ القَدِيمَةِ في الدَّوْلَة، بِنَاءُ السُّفُنْ ، بِنَاءُ العَرِيِشْ ، و صِنَاعَةْ الفَخَّارْ و هُنَاكَ الكَثِيِرْ مِن المِهَنْ');

-- --------------------------------------------------------

--
-- Table structure for table `userunion`
--

CREATE TABLE `userunion` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userunion`
--

INSERT INTO `userunion` (`id`, `phrase`) VALUES
(1, 'في الثاني من ديسمبر 1971 ارتفع عَلَمُ دولة الإماراتِ العربية المتحدة للمرة الأولى على سارية قصر الاتحاد بمنطقة الجُمِيرَا في دبي، ليعلن للعالم أجمع قيام الدولة الاتحادية\n'),
(2, 'في ٢ ديسمبر سنةْ 1971 عقد حكام الإمارات الست اجتماعاً وأعلنوا سَرَيَان مفعول الدستور المؤقت وقيام دولة الإمارات العربية المتحدة، و انضمت إليها إمارة رأس الخيمة في 10 فبراير 1972.');

-- --------------------------------------------------------

--
-- Table structure for table `userunited`
--

CREATE TABLE `userunited` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userunited`
--

INSERT INTO `userunited` (`id`, `phrase`) VALUES
(1, 'تتألف دولة الإمارات العربية المتحدة من سبع إمارات هي: أبو ظبي ودبي، والشارقة، ورأس الخيمة، وعجمان، وأم القِيوِيِنْ ، و الفجيرة');

-- --------------------------------------------------------

--
-- Table structure for table `userwaits`
--

CREATE TABLE `userwaits` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userwaits`
--

INSERT INTO `userwaits` (`id`, `phrase`) VALUES
(1, 'أُقَدِّرُ صَبْرُك. أتمنى أن يكون لَدَيْ ما تحتاج إِلَيْهِ قَرِيباً.\n'),
(2, 'شُكْراً لكونك صَبُوراً جدا. في بعض الأحيان تستغرق هذه الأشياء بعض الوَقْتْ.\n');

-- --------------------------------------------------------

--
-- Table structure for table `userwantstoseeagentagain`
--

CREATE TABLE `userwantstoseeagentagain` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userwantstoseeagentagain`
--

INSERT INTO `userwantstoseeagentagain` (`id`, `phrase`) VALUES
(1, 'إِطْلاقَاً! سأعول عليه.\n'),
(2, '.في أي وَقْتْ. لقد حَظِيّنَا وَقْتَاً مُمْتِعَاً حتى الآنْ.\n'),
(3, 'بالتَأكِيدْ. اَسْتَمْتِعُ بالحديث مَعَكْ. آمل أن أراك مَرَّةً أخرى قَرِيبَاً.\n'),
(4, ' بالتأكيد نأمل ذلك. أنا دَائِماً هُنَا كلما كنت في حاجة لي.\n');

-- --------------------------------------------------------

--
-- Table structure for table `userwantstotalk`
--

CREATE TABLE `userwantstotalk` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userwantstotalk`
--

INSERT INTO `userwantstotalk` (`id`, `phrase`) VALUES
(1, 'أنا هنا للدردشة في أي وقت تُرِيدْ.\n'),
(2, 'محادثة جيدة حقا.\n'),
(3, 'أنا دَائِماً هُنا لإعطاء الإِذن.\n'),
(4, 'الحديث هو أفضل ما أَفْعَلُهْ.\n');

-- --------------------------------------------------------

--
-- Table structure for table `userwhatdoyouknowaboutkhwarizmi`
--

CREATE TABLE `userwhatdoyouknowaboutkhwarizmi` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userwhatdoyouknowaboutkhwarizmi`
--

INSERT INTO `userwhatdoyouknowaboutkhwarizmi` (`id`, `phrase`) VALUES
(1, 'يُعْتَبَرُ مِنْ أوَائِلِ عُلَمَاءِ الرِّيَاضِيَّاتِ الْمُسلمينْ, حَيْثُ سَاهَمَتْ أَعْمَالُهُ بِدَورٍ كَبِيرٍ فِي تَقَدُّمِ الرِّيَاضِيَّاتِ فِي عَصْرِهْ. عَمِلَ فِي بَيْتِ الْحِكْمَةِ فِي بَغْدَادْ, وَ كَسِبَ ثِقَةِ الْخَلِيفَةِ إِذْ عَهِدَ إِلَيْهِ بِرَ');

-- --------------------------------------------------------

--
-- Table structure for table `userwillbeback`
--

CREATE TABLE `userwillbeback` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userwillbeback`
--

INSERT INTO `userwillbeback` (`id`, `phrase`) VALUES
(1, 'سوف أكون في انْتِظارِكْ.\n'),
(2, 'حَسَنَاً. أَنْتَ تعرف أَيْنَ تَجِدُنِي.\n'),
(3, 'حَسَنَاً. سأكون هنا.\n'),
(4, 'حَسَنَاً. أنا دَائِماً هنا.\n');

-- --------------------------------------------------------

--
-- Table structure for table `userzayed`
--

CREATE TABLE `userzayed` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userzayed`
--

INSERT INTO `userzayed` (`id`, `phrase`) VALUES
(1, 'ولد المغفور له الشيخ زايد بن سلطان آل نهيان، رحمه الله، مؤسس دولة الإمارات العربية المتحدة، في مدينة أبوظبي عام 1918، حَكَمَ أبوظبي بين عامي 1966 وحتى وفاته عام 2004، وسمي تَيَمُّنَاً بجده الشيخ زايد بن خليفة آل نهيان.\n'),
(2, 'الشيخ زايد بن سلطان آل نهيان هو مُؤَسِّسْ دولة الإمارات العربية المتحدة ،,, وولد في عام 1918 ميلادي في أبو ظبي، وهو أول رئيس لدولة الإمارات\n');

-- --------------------------------------------------------

--
-- Table structure for table `userzayedachiv`
--

CREATE TABLE `userzayedachiv` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userzayedachiv`
--

INSERT INTO `userzayedachiv` (`id`, `phrase`) VALUES
(1, 'من أبرز أعمال الشيخ زايد رحمه الله، تأسيسه لمجلس التعاون لدول الخليج العربية، وهو صانع الاتحاد،\n'),
(2, ' حرص المغفور له الشيخ زايد بن سلطان آل نهيان، منذ توليه مقاليد الحُكْمْ في إمارة أبوظبي عام 1966، على الاهتمام بالقضايا البِيِئِيَّة ، حيث تم حظر الصيد في إمارة أبوظبي منذ عام 1977، فَضْلاً عن جهوده في زراعة الصحراء، والتي تُعْتَبَرْ من أهم الإنجازات الخا'),
(3, ' كان للشيخ زايد رحمه الله دور كبير لتعليم المرأة، بالإضافة إلى إعداد المستشفيات المتطورة الموجودة في جميع أنحاء الدولة\n'),
(4, 'كلف حُكُومَتِهِ ببناء وتعزيز قدرات الدولة في مجال الصحة والتعليم والعدالة والرعاية الاجتماعية، وتوفير الفرص لجميع مواطني الدولة من أجل أن يكون لهم دَوْراً فعّالاً في نجاح الأمة\n'),
(5, 'عَلَى المستوى الخارجي وضع المغفور له الشيخ زايد . أسس سياسة خارجية متميزة تتسم بالحِكْمَةِ والاعتدال، والتوازن، ومناصرة الحق والعدالة\n'),
(6, 'من الناحية الاقتصادية، نجح الشيخ زايد، رحمه الله، في توظيف عائدات النفط في بناء اقتصاد قوي ومتماسك مما وضع دولة الإمارات العربية المتحدة في مصاف الدول المتطورة إقْتِصَادِياً في المنطقة');

-- --------------------------------------------------------

--
-- Table structure for table `usredidyouhearme`
--

CREATE TABLE `usredidyouhearme` (
  `id` int(11) NOT NULL,
  `phrase` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `usredidyouhearme`
--

INSERT INTO `usredidyouhearme` (`id`, `phrase`) VALUES
(1, 'نَعَمْ, أسمَعُكَّ بِوضوحْ\r\n'),
(2, 'نَعَمْ, أسمَعُكَّ ');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `agentacquaintance`
--
ALTER TABLE `agentacquaintance`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `agentage`
--
ALTER TABLE `agentage`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `agentanswermyquestion`
--
ALTER TABLE `agentanswermyquestion`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `agentboring`
--
ALTER TABLE `agentboring`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `agentcanyouhelp`
--
ALTER TABLE `agentcanyouhelp`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `agentclever`
--
ALTER TABLE `agentclever`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `agentgood`
--
ALTER TABLE `agentgood`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `agenthappy`
--
ALTER TABLE `agenthappy`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `agenthobby`
--
ALTER TABLE `agenthobby`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `agentmyfriend`
--
ALTER TABLE `agentmyfriend`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `agentorigin`
--
ALTER TABLE `agentorigin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `agentready`
--
ALTER TABLE `agentready`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `agenttalktome`
--
ALTER TABLE `agenttalktome`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `agentthere`
--
ALTER TABLE `agentthere`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `appraisalbad`
--
ALTER TABLE `appraisalbad`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `appraisalgood`
--
ALTER TABLE `appraisalgood`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `appraisalnoproblem`
--
ALTER TABLE `appraisalnoproblem`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `appraisalthankyou`
--
ALTER TABLE `appraisalthankyou`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `appraisalwelldone`
--
ALTER TABLE `appraisalwelldone`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `contributions`
--
ALTER TABLE `contributions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dialogholdon`
--
ALTER TABLE `dialogholdon`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dialogidonotcare`
--
ALTER TABLE `dialogidonotcare`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dialogsorry`
--
ALTER TABLE `dialogsorry`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dialogwhatdoyoumean`
--
ALTER TABLE `dialogwhatdoyoumean`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dialogwrong`
--
ALTER TABLE `dialogwrong`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `greetingsbye`
--
ALTER TABLE `greetingsbye`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `greetingsgoodevening`
--
ALTER TABLE `greetingsgoodevening`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `greetingsgoodmorning`
--
ALTER TABLE `greetingsgoodmorning`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `greetingsgoodnight`
--
ALTER TABLE `greetingsgoodnight`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `greetingshello`
--
ALTER TABLE `greetingshello`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `greetingshowareyou`
--
ALTER TABLE `greetingshowareyou`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `greetingsniceto`
--
ALTER TABLE `greetingsniceto`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `salam`
--
ALTER TABLE `salam`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userback`
--
ALTER TABLE `userback`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userbored`
--
ALTER TABLE `userbored`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userbrqaa`
--
ALTER TABLE `userbrqaa`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `usercallingrobot`
--
ALTER TABLE `usercallingrobot`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `usercanyouseeme`
--
ALTER TABLE `usercanyouseeme`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `usercapital`
--
ALTER TABLE `usercapital`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userculture`
--
ALTER TABLE `userculture`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userdance`
--
ALTER TABLE `userdance`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userdoyouknowme`
--
ALTER TABLE `userdoyouknowme`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userexcited`
--
ALTER TABLE `userexcited`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userflag`
--
ALTER TABLE `userflag`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userfood`
--
ALTER TABLE `userfood`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `usergames`
--
ALTER TABLE `usergames`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `usergeography`
--
ALTER TABLE `usergeography`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `usergood`
--
ALTER TABLE `usergood`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userhappy`
--
ALTER TABLE `userhappy`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userhasbirthday`
--
ALTER TABLE `userhasbirthday`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userhere`
--
ALTER TABLE `userhere`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userhighestbuilding`
--
ALTER TABLE `userhighestbuilding`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userjoking`
--
ALTER TABLE `userjoking`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userlanguage`
--
ALTER TABLE `userlanguage`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `usermath`
--
ALTER TABLE `usermath`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `usermenclothes`
--
ALTER TABLE `usermenclothes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `usermodernsites`
--
ALTER TABLE `usermodernsites`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userneedsadvice`
--
ALTER TABLE `userneedsadvice`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `usersites`
--
ALTER TABLE `usersites`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `usersofia`
--
ALTER TABLE `usersofia`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userspace`
--
ALTER TABLE `userspace`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `usertestingagent`
--
ALTER TABLE `usertestingagent`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `usertraditionsjobs`
--
ALTER TABLE `usertraditionsjobs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userunion`
--
ALTER TABLE `userunion`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userunited`
--
ALTER TABLE `userunited`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userwaits`
--
ALTER TABLE `userwaits`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userwantstoseeagentagain`
--
ALTER TABLE `userwantstoseeagentagain`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userwantstotalk`
--
ALTER TABLE `userwantstotalk`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userwhatdoyouknowaboutkhwarizmi`
--
ALTER TABLE `userwhatdoyouknowaboutkhwarizmi`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userwillbeback`
--
ALTER TABLE `userwillbeback`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userzayed`
--
ALTER TABLE `userzayed`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userzayedachiv`
--
ALTER TABLE `userzayedachiv`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `usredidyouhearme`
--
ALTER TABLE `usredidyouhearme`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `agentacquaintance`
--
ALTER TABLE `agentacquaintance`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `agentage`
--
ALTER TABLE `agentage`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `agentanswermyquestion`
--
ALTER TABLE `agentanswermyquestion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `agentboring`
--
ALTER TABLE `agentboring`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `agentcanyouhelp`
--
ALTER TABLE `agentcanyouhelp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `agentclever`
--
ALTER TABLE `agentclever`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `agentgood`
--
ALTER TABLE `agentgood`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `agenthappy`
--
ALTER TABLE `agenthappy`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `agenthobby`
--
ALTER TABLE `agenthobby`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `agentmyfriend`
--
ALTER TABLE `agentmyfriend`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `agentorigin`
--
ALTER TABLE `agentorigin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `agentready`
--
ALTER TABLE `agentready`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `agenttalktome`
--
ALTER TABLE `agenttalktome`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `agentthere`
--
ALTER TABLE `agentthere`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `appraisalbad`
--
ALTER TABLE `appraisalbad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `appraisalgood`
--
ALTER TABLE `appraisalgood`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `appraisalnoproblem`
--
ALTER TABLE `appraisalnoproblem`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `appraisalthankyou`
--
ALTER TABLE `appraisalthankyou`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `appraisalwelldone`
--
ALTER TABLE `appraisalwelldone`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `contributions`
--
ALTER TABLE `contributions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `dialogholdon`
--
ALTER TABLE `dialogholdon`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `dialogidonotcare`
--
ALTER TABLE `dialogidonotcare`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `dialogsorry`
--
ALTER TABLE `dialogsorry`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `dialogwhatdoyoumean`
--
ALTER TABLE `dialogwhatdoyoumean`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `dialogwrong`
--
ALTER TABLE `dialogwrong`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `greetingsbye`
--
ALTER TABLE `greetingsbye`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `greetingsgoodevening`
--
ALTER TABLE `greetingsgoodevening`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `greetingsgoodmorning`
--
ALTER TABLE `greetingsgoodmorning`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `greetingsgoodnight`
--
ALTER TABLE `greetingsgoodnight`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `greetingshello`
--
ALTER TABLE `greetingshello`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `greetingshowareyou`
--
ALTER TABLE `greetingshowareyou`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `greetingsniceto`
--
ALTER TABLE `greetingsniceto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `salam`
--
ALTER TABLE `salam`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `userback`
--
ALTER TABLE `userback`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `userbored`
--
ALTER TABLE `userbored`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `userbrqaa`
--
ALTER TABLE `userbrqaa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `usercallingrobot`
--
ALTER TABLE `usercallingrobot`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `usercanyouseeme`
--
ALTER TABLE `usercanyouseeme`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `usercapital`
--
ALTER TABLE `usercapital`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `userculture`
--
ALTER TABLE `userculture`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `userdance`
--
ALTER TABLE `userdance`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `userdoyouknowme`
--
ALTER TABLE `userdoyouknowme`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `userexcited`
--
ALTER TABLE `userexcited`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `userflag`
--
ALTER TABLE `userflag`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `userfood`
--
ALTER TABLE `userfood`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `usergames`
--
ALTER TABLE `usergames`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `usergeography`
--
ALTER TABLE `usergeography`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `usergood`
--
ALTER TABLE `usergood`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `userhappy`
--
ALTER TABLE `userhappy`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `userhasbirthday`
--
ALTER TABLE `userhasbirthday`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `userhere`
--
ALTER TABLE `userhere`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `userhighestbuilding`
--
ALTER TABLE `userhighestbuilding`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `userjoking`
--
ALTER TABLE `userjoking`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `userlanguage`
--
ALTER TABLE `userlanguage`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `usermath`
--
ALTER TABLE `usermath`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `usermenclothes`
--
ALTER TABLE `usermenclothes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `usermodernsites`
--
ALTER TABLE `usermodernsites`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `userneedsadvice`
--
ALTER TABLE `userneedsadvice`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `usersites`
--
ALTER TABLE `usersites`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `usersofia`
--
ALTER TABLE `usersofia`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `userspace`
--
ALTER TABLE `userspace`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `usertestingagent`
--
ALTER TABLE `usertestingagent`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `usertraditionsjobs`
--
ALTER TABLE `usertraditionsjobs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `userunion`
--
ALTER TABLE `userunion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `userunited`
--
ALTER TABLE `userunited`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `userwaits`
--
ALTER TABLE `userwaits`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `userwantstoseeagentagain`
--
ALTER TABLE `userwantstoseeagentagain`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `userwantstotalk`
--
ALTER TABLE `userwantstotalk`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `userwhatdoyouknowaboutkhwarizmi`
--
ALTER TABLE `userwhatdoyouknowaboutkhwarizmi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `userwillbeback`
--
ALTER TABLE `userwillbeback`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `userzayed`
--
ALTER TABLE `userzayed`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `userzayedachiv`
--
ALTER TABLE `userzayedachiv`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `usredidyouhearme`
--
ALTER TABLE `usredidyouhearme`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
