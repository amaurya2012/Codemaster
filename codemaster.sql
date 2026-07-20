-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3308:3308
-- Generation Time: Feb 20, 2026 at 04:21 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `codemaster`
--
create database codemaster;
use codemaster;
-- --------------------------------------------------------

--
-- Table structure for table `problem`
--

CREATE TABLE `problem` (
  `id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` text NOT NULL,
  `difficulty` varchar(10) NOT NULL,
  `marks` int(11) NOT NULL,
  `sample_input` text DEFAULT NULL,
  `sample_output` text DEFAULT NULL,
  `input_data` text NOT NULL,
  `expected_output` text NOT NULL,
  `hidden_input` text NOT NULL,
  `hidden_output` text NOT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `problem`
--

INSERT INTO `problem` (`id`, `title`, `description`, `difficulty`, `marks`, `sample_input`, `sample_output`, `input_data`, `expected_output`, `hidden_input`, `hidden_output`, `created_at`) VALUES
(1, 'Sum of Digits', 'Given a non-negative integer N, find the sum of its digits.\r\n\r\nInput will contain a single integer N.\r\nOutput should be the sum of all digits in the number.', 'Easy', 10, '1234', '10', '5\r\n99\r\n1001', '5\r\n18\r\n2', '5\r\n18\r\n2', '5\r\n9\r\n2', '2026-02-19 12:18:35'),
(2, 'Reverse a Number', 'Given a non-negative integer N, reverse the digits of the number.\r\n\r\nThe reversed number should not contain leading zeros.', 'Easy', 10, '12345', '54321', '120\r\n405\r\n9', '21\r\n504\r\n9', '1000\r\n70001\r\n0', '1\r\n10007\r\n0', '2026-02-19 12:27:21'),
(3, 'Sum of Two Numbers', 'Two integers separated by a space.', 'Easy', 5, '5 7', '12', '5 7\r\n10 20', '12\r\n30', '100 200\r\n-5 3', '300\r\n-2', '2026-02-20 14:27:38');

-- --------------------------------------------------------

--
-- Table structure for table `submission`
--

CREATE TABLE `submission` (
  `id` int(11) NOT NULL,
  `code` text NOT NULL,
  `language` varchar(20) NOT NULL,
  `status` varchar(30) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `problem_id` int(11) NOT NULL,
  `submitted_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `submission`
--

INSERT INTO `submission` (`id`, `code`, `language`, `status`, `score`, `user_id`, `problem_id`, `submitted_at`) VALUES
(1, 'n = input().strip()\r\ns = 0\r\nfor ch in n:\r\n    s += int(ch)\r\nprint(s)', 'python', 'Wrong Answer', 5, 2, 1, '2026-02-19 12:21:29'),
(2, '#include <stdio.h>\r\n\r\nint main() {\r\n    long long n;\r\n    int sum = 0;\r\n    scanf(\"%lld\", &n);\r\n\r\n    while (n > 0) {\r\n        sum += n % 10;\r\n        n /= 10;\r\n    }\r\n\r\n    printf(\"%d\", sum);\r\n    return 0;\r\n}', 'c', 'Wrong Answer', 5, 2, 1, '2026-02-19 12:22:32'),
(3, '#include <stdio.h>\r\n\r\nint main() {\r\n    long long n;\r\n    int sum = 0;\r\n    scanf(\"%lld\", &n);\r\n\r\n    while (n > 0) {\r\n        sum += n % 10;\r\n        n /= 10;\r\n    }\r\n\r\n    printf(\"%d\", sum);\r\n    return 0;\r\n}', 'c', 'Wrong Answer', 5, 2, 1, '2026-02-19 12:24:57'),
(4, '#include <stdio.h>\r\n\r\nint main() {\r\n    long long n;\r\n    int sum = 0;\r\n    scanf(\"%lld\", &n);\r\n\r\n    while (n > 0) {\r\n        sum += n % 10;\r\n        n /= 10;\r\n    }\r\n\r\n    printf(\"%d\", sum);\r\n    return 0;\r\n}', 'c', 'Wrong Answer', 5, 2, 1, '2026-02-19 12:25:03'),
(5, 'n = input().strip()\r\nrev = n[::-1]\r\nrev = rev.lstrip(\'0\')\r\nprint(rev if rev else \"0\")', 'python', 'Accepted', 10, 2, 2, '2026-02-19 12:28:06'),
(6, 'n = input().strip()\r\nrev = n[::1]\r\nrev = rev.lstrip(\'0\')\r\nprint(rev if rev else \"0\")', 'python', 'Wrong Answer', 3, 2, 2, '2026-02-19 12:28:18'),
(7, 'n = input().strip()\r\nrev = n[::-1]\r\nrev = rev.lstrip(\'0\')\r\n     print(rev if rev else \"0\")', 'python', 'Wrong Answer', 0, 2, 2, '2026-02-19 12:31:12'),
(8, 'n = inpu().strip()\r\nrev = n[::-1]\r\nrev = rev.lstrip(\'0\')\r\nprint(rev if rev else \"0\")\r\n', 'python', 'Wrong Answer', 0, 2, 2, '2026-02-19 12:31:33'),
(9, 'n = inpu().strip()\r\nrev = n[::-1]\r\nrev = rev.lstrip(\'0\')\r\nprint(rev if rev else \"0\")\r\n', 'python', 'Wrong Answer', 0, 2, 2, '2026-02-19 12:32:42'),
(10, 'n = input().strip()\r\nrev = n[::-1]\r\nrev = rev.lstrip(\'0\')\r\nprint(rev if rev else \"0\")', 'python', 'Accepted', 10, 2, 2, '2026-02-19 13:00:24'),
(11, '#include <stdio.h>\r\n\r\nint main() {\r\n    long long n, rev = 0;\r\n    scanf(\"%lld\", &n);\r\n\r\n    if (n == 0) {\r\n        printf(\"0\");\r\n        return 0;\r\n    }\r\n\r\n    while (n > 0) {\r\n        rev = rev * 10 + (n % 10);\r\n        n /= 10;\r\n    }\r\n\r\n    printf(\"%lld\", rev);\r\n    return 0;\r\n}\r\n', 'c', 'Accepted', 10, 2, 2, '2026-02-19 13:02:34'),
(12, 'n = input().strip()\r\ns = 0\r\nfor ch in n:\r\n    s += int(ch)\r\nprint(s)', 'python', 'Wrong Answer', 5, 2, 1, '2026-02-20 14:14:23'),
(13, 'a,b=map(int,input()).split()\r\nprint(a+b)', 'python', 'Wrong Answer', 0, 2, 3, '2026-02-20 14:29:03'),
(14, 'a,b=map(int,input().split())\r\nprint(a+b)', 'python', 'Accepted', 5, 2, 3, '2026-02-20 14:30:30');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `email` varchar(120) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `role` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `password_hash`, `role`) VALUES
(1, 'admin', 'admin@gmail.com', 'pbkdf2:sha256:600000$RILSCLmRb2nAVP80$0e731f2a995564bc2250086a502312c88a7af58dad73b3a8e2799e407a8b7ddf', 'admin'),
(2, 'ram', 'ram@gmail.com', 'pbkdf2:sha256:600000$DLzfXYzJ2X0Sp97T$378a28ef906f86190c588fa0ac0bc9714a7df5fbb8f857b1d6b0c6b916f40af6', 'user');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `problem`
--
ALTER TABLE `problem`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `submission`
--
ALTER TABLE `submission`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `problem_id` (`problem_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `problem`
--
ALTER TABLE `problem`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `submission`
--
ALTER TABLE `submission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `submission`
--
ALTER TABLE `submission`
  ADD CONSTRAINT `submission_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `submission_ibfk_2` FOREIGN KEY (`problem_id`) REFERENCES `problem` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
