-- ============================================
-- CourseWeave AI - Seed Data
-- Real Northeastern University courses scraped 
-- from catalog.northeastern.edu
-- ============================================

-- ============================================
-- COURSES (Real NEU courses)
-- ============================================

INSERT INTO courses (course_code, course_name, credits, program_code, course_type) VALUES

-- MS Data Analytics Engineering (MS_DAE) Core
('IE6400', 'Foundations of Data Analytics Engineering', 4, 'MS_DAE', 'Core'),
('IE6700', 'Data Management and Database Design', 4, 'MS_DAE', 'Core'),
('IE7275', 'Data Mining in Engineering', 4, 'MS_DAE', 'Core'),
('IE6600', 'Computation and Visualization for Analytics', 4, 'MS_DAE', 'Core'),
('IE6200', 'Engineering Probability and Statistics', 4, 'MS_DAE', 'Core'),

-- MS Data Analytics Engineering Electives
('IE7615', 'Neural Networks and Deep Learning', 4, 'MS_DAE', 'Elective'),
('IE7500', 'Applied Natural Language Processing', 4, 'MS_DAE', 'Elective'),
('IE6750', 'Data Warehousing and Integration', 4, 'MS_DAE', 'Elective'),
('IE7215', 'Applied Statistics for Engineering', 4, 'MS_DAE', 'Elective'),
('IE7285', 'Statistical Quality Control', 4, 'MS_DAE', 'Elective'),
('IE7200', 'Supply Chain Engineering', 4, 'MS_DAE', 'Elective'),
('IE5200', 'Mathematics for Machine Learning', 4, 'MS_DAE', 'Elective'),

-- MS Data Analytics (DA prefix)
('DA5020', 'Collecting, Storing, and Retrieving Data', 4, 'MS_DA', 'Core'),
('DA5030', 'Introduction to Data Mining and Machine Learning', 4, 'MS_DA', 'Core'),

-- MS Data Science (DS prefix)
('DS5110', 'Introduction to Data Management and Processing', 4, 'MS_DS', 'Core'),
('DS5220', 'Supervised Machine Learning and Learning Theory', 4, 'MS_DS', 'Core'),
('DS5230', 'Unsupervised Machine Learning and Data Mining', 4, 'MS_DS', 'Elective'),
('DS5500', 'Data Science Capstone', 4, 'MS_DS', 'Core'),

-- CS courses
('CS6140', 'Machine Learning', 4, 'MS_CS', 'Core'),
('CS6220', 'Data Mining Techniques', 4, 'MS_CS', 'Elective'),
('CS5800', 'Algorithms', 4, 'MS_CS', 'Core'),
('CS6120', 'Natural Language Processing', 4, 'MS_CS', 'Elective'),
('CS7150', 'Deep Learning', 4, 'MS_CS', 'Elective'),

-- DAMG courses
('DAMG7370', 'Designing Advanced Data Architectures for Business Intelligence', 4, 'MS_IS', 'Core'),
('DAMG6210', 'Managing Data and Organizations', 4, 'MS_IS', 'Core');

-- ============================================
-- PREREQUISITES (Real NEU prerequisite rules)
-- ============================================

INSERT INTO prerequisites (course_code, required_course_code) VALUES
('IE7275', 'IE6400'),
('IE7615', 'IE7275'),
('IE7500', 'IE7275'),
('IE6750', 'IE6700'),
('IE7215', 'IE6200'),
('IE7285', 'IE6200'),
('IE7200', 'IE6200'),
('DA5030', 'DA5020'),
('DS5220', 'DS5110'),
('DS5230', 'DS5110'),
('CS6220', 'CS6140');

-- ============================================
-- CAREERS
-- ============================================

-- stored as simple strings in students table
-- career options:
-- 'Data Analyst'
-- 'Data Engineer'
-- 'Data Scientist'
-- 'Business Analyst'
-- 'Software Engineer'

-- ============================================
-- STUDENTS (100 realistic dummy students)
-- ============================================

INSERT INTO students (name, email, program_code, target_career) VALUES
('Aisha Patel', 'patel.ai@northeastern.edu', 'MS_DAE', 'Data Engineer'),
('Carlos Mendez', 'mendez.c@northeastern.edu', 'MS_DAE', 'Data Scientist'),
('Wei Zhang', 'zhang.w@northeastern.edu', 'MS_CS', 'Software Engineer'),
('Priya Sharma', 'sharma.p@northeastern.edu', 'MS_DAE', 'Data Analyst'),
('James O''Brien', 'obrien.j@northeastern.edu', 'MS_DS', 'Data Scientist'),
('Fatima Al-Hassan', 'alhassan.f@northeastern.edu', 'MS_DAE', 'Data Engineer'),
('Raj Krishnamurthy', 'krishnamurthy.r@northeastern.edu', 'MS_CS', 'Data Scientist'),
('Sofia Rossi', 'rossi.s@northeastern.edu', 'MS_DA', 'Business Analyst'),
('Ahmed Khalil', 'khalil.a@northeastern.edu', 'MS_DAE', 'Data Engineer'),
('Emma Thompson', 'thompson.e@northeastern.edu', 'MS_DS', 'Data Scientist'),
('Yuki Tanaka', 'tanaka.y@northeastern.edu', 'MS_CS', 'Software Engineer'),
('Maria Santos', 'santos.m@northeastern.edu', 'MS_DA', 'Data Analyst'),
('Kevin Park', 'park.k@northeastern.edu', 'MS_DAE', 'Data Engineer'),
('Nia Johnson', 'johnson.n@northeastern.edu', 'MS_DS', 'Data Scientist'),
('Arjun Nair', 'nair.a@northeastern.edu', 'MS_DAE', 'Data Analyst'),
('Isabella Ferreira', 'ferreira.i@northeastern.edu', 'MS_DA', 'Business Analyst'),
('Mohammed Rahman', 'rahman.m@northeastern.edu', 'MS_CS', 'Software Engineer'),
('Lin Chen', 'chen.l@northeastern.edu', 'MS_DAE', 'Data Engineer'),
('Zara Ahmed', 'ahmed.z@northeastern.edu', 'MS_DS', 'Data Scientist'),
('Lucas Silva', 'silva.l@northeastern.edu', 'MS_DA', 'Data Analyst'),
('Ananya Gupta', 'gupta.a@northeastern.edu', 'MS_DAE', 'Data Scientist'),
('Ryan Murphy', 'murphy.r@northeastern.edu', 'MS_CS', 'Software Engineer'),
('Mei Liu', 'liu.m@northeastern.edu', 'MS_DAE', 'Data Engineer'),
('Amara Osei', 'osei.a@northeastern.edu', 'MS_DS', 'Data Scientist'),
('Daniel Kim', 'kim.d@northeastern.edu', 'MS_DAE', 'Data Analyst'),
('Valentina Cruz', 'cruz.v@northeastern.edu', 'MS_DA', 'Business Analyst'),
('Siddharth Joshi', 'joshi.s@northeastern.edu', 'MS_CS', 'Software Engineer'),
('Yara Ibrahim', 'ibrahim.y@northeastern.edu', 'MS_DAE', 'Data Engineer'),
('Thomas Anderson', 'anderson.t@northeastern.edu', 'MS_DS', 'Data Scientist'),
('Sakura Yamamoto', 'yamamoto.s@northeastern.edu', 'MS_DA', 'Data Analyst'),
('Kwame Mensah', 'mensah.k@northeastern.edu', 'MS_DAE', 'Data Engineer'),
('Elena Petrov', 'petrov.e@northeastern.edu', 'MS_CS', 'Software Engineer'),
('Ravi Chandrasekaran', 'chandrasekaran.r@northeastern.edu', 'MS_DAE', 'Data Scientist'),
('Amelia Clarke', 'clarke.a@northeastern.edu', 'MS_DS', 'Data Scientist'),
('Omar Abdullah', 'abdullah.o@northeastern.edu', 'MS_DAE', 'Data Engineer'),
('Nadia Kowalski', 'kowalski.n@northeastern.edu', 'MS_DA', 'Business Analyst'),
('Ethan Williams', 'williams.e@northeastern.edu', 'MS_CS', 'Software Engineer'),
('Divya Menon', 'menon.d@northeastern.edu', 'MS_DAE', 'Data Analyst'),
('Santiago Gomez', 'gomez.s@northeastern.edu', 'MS_DS', 'Data Scientist'),
('Hana Nakamura', 'nakamura.h@northeastern.edu', 'MS_DA', 'Data Analyst'),
('Tariq Hassan', 'hassan.t@northeastern.edu', 'MS_DAE', 'Data Engineer'),
('Olivia Martin', 'martin.o@northeastern.edu', 'MS_CS', 'Software Engineer'),
('Vikram Singh', 'singh.v@northeastern.edu', 'MS_DAE', 'Data Scientist'),
('Chiara Romano', 'romano.c@northeastern.edu', 'MS_DS', 'Data Scientist'),
('Bashir Ali', 'ali.b@northeastern.edu', 'MS_DAE', 'Data Engineer'),
('Ingrid Hansen', 'hansen.i@northeastern.edu', 'MS_DA', 'Business Analyst'),
('Aditya Kumar', 'kumar.a@northeastern.edu', 'MS_CS', 'Software Engineer'),
('Zoe Wilson', 'wilson.z@northeastern.edu', 'MS_DAE', 'Data Analyst'),
('Youssef Mansour', 'mansour.y@northeastern.edu', 'MS_DS', 'Data Scientist'),
('Akiko Suzuki', 'suzuki.a@northeastern.edu', 'MS_DA', 'Data Analyst'),
('Kofi Asante', 'asante.k@northeastern.edu', 'MS_DAE', 'Data Engineer'),
('Anastasia Volkov', 'volkov.a@northeastern.edu', 'MS_CS', 'Software Engineer'),
('Rohan Desai', 'desai.r@northeastern.edu', 'MS_DAE', 'Data Scientist'),
('Camille Dubois', 'dubois.c@northeastern.edu', 'MS_DS', 'Data Scientist'),
('Hamid Rahimi', 'rahimi.h@northeastern.edu', 'MS_DAE', 'Data Engineer'),
('Freya Andersen', 'andersen.f@northeastern.edu', 'MS_DA', 'Business Analyst'),
('Nikhil Reddy', 'reddy.n@northeastern.edu', 'MS_CS', 'Software Engineer'),
('Maya Robinson', 'robinson.m@northeastern.edu', 'MS_DAE', 'Data Analyst'),
('Ali Hassan', 'hassan.a@northeastern.edu', 'MS_DS', 'Data Scientist'),
('Yuki Watanabe', 'watanabe.y@northeastern.edu', 'MS_DA', 'Data Analyst'),
('Kwabena Owusu', 'owusu.k@northeastern.edu', 'MS_DAE', 'Data Engineer'),
('Vera Sokolova', 'sokolova.v@northeastern.edu', 'MS_CS', 'Software Engineer'),
('Pranav Pillai', 'pillai.p@northeastern.edu', 'MS_DAE', 'Data Scientist'),
('Lucia Moretti', 'moretti.l@northeastern.edu', 'MS_DS', 'Data Scientist'),
('Karim Benali', 'benali.k@northeastern.edu', 'MS_DAE', 'Data Engineer'),
('Astrid Lindqvist', 'lindqvist.a@northeastern.edu', 'MS_DA', 'Business Analyst'),
('Vivek Iyer', 'iyer.v@northeastern.edu', 'MS_CS', 'Software Engineer'),
('Grace Lee', 'lee.g@northeastern.edu', 'MS_DAE', 'Data Analyst'),
('Hassan Al-Farsi', 'alfarsi.h@northeastern.edu', 'MS_DS', 'Data Scientist'),
('Yuna Kim', 'kim.y@northeastern.edu', 'MS_DA', 'Data Analyst'),
('Ade Okonkwo', 'okonkwo.a@northeastern.edu', 'MS_DAE', 'Data Engineer'),
('Katya Morozova', 'morozova.k@northeastern.edu', 'MS_CS', 'Software Engineer'),
('Suresh Babu', 'babu.s@northeastern.edu', 'MS_DAE', 'Data Scientist'),
('Francesca Esposito', 'esposito.f@northeastern.edu', 'MS_DS', 'Data Scientist'),
('Tariq Al-Rashid', 'alrashid.t@northeastern.edu', 'MS_DAE', 'Data Engineer'),
('Sigrid Eriksson', 'eriksson.s@northeastern.edu', 'MS_DA', 'Business Analyst'),
('Karthik Subramanian', 'subramanian.k@northeastern.edu', 'MS_CS', 'Software Engineer'),
('Lily Chen', 'chen.li@northeastern.edu', 'MS_DAE', 'Data Analyst'),
('Faisal Al-Amin', 'alamin.f@northeastern.edu', 'MS_DS', 'Data Scientist'),
('Mina Tanaka', 'tanaka.m@northeastern.edu', 'MS_DA', 'Data Analyst'),
('Emeka Eze', 'eze.e@northeastern.edu', 'MS_DAE', 'Data Engineer'),
('Polina Ivanova', 'ivanova.p@northeastern.edu', 'MS_CS', 'Software Engineer'),
('Aryan Kapoor', 'kapoor.a@northeastern.edu', 'MS_DAE', 'Data Scientist'),
('Giulia Ferrari', 'ferrari.g@northeastern.edu', 'MS_DS', 'Data Scientist'),
('Samir Khalid', 'khalid.s@northeastern.edu', 'MS_DAE', 'Data Engineer'),
('Maja Karlsson', 'karlsson.m@northeastern.edu', 'MS_DA', 'Business Analyst'),
('Rahul Bose', 'bose.r@northeastern.edu', 'MS_CS', 'Software Engineer'),
('Hannah Green', 'green.h@northeastern.edu', 'MS_DAE', 'Data Analyst'),
('Younes Benali', 'benali.y@northeastern.edu', 'MS_DS', 'Data Scientist'),
('Riko Hayashi', 'hayashi.r@northeastern.edu', 'MS_DA', 'Data Analyst'),
('Chidi Obi', 'obi.c@northeastern.edu', 'MS_DAE', 'Data Engineer'),
('Natasha Petrov', 'petrov.n@northeastern.edu', 'MS_CS', 'Software Engineer'),
('Deepak Nambiar', 'nambiar.d@northeastern.edu', 'MS_DAE', 'Data Scientist'),
('Sara Conti', 'conti.s@northeastern.edu', 'MS_DS', 'Data Scientist'),
('Bilal Qureshi', 'qureshi.b@northeastern.edu', 'MS_DAE', 'Data Engineer'),
('Lena Johansson', 'johansson.l@northeastern.edu', 'MS_DA', 'Business Analyst'),
('Arun Venkatesh', 'venkatesh.a@northeastern.edu', 'MS_CS', 'Software Engineer'),
('Clara Hoffman', 'hoffman.c@northeastern.edu', 'MS_DAE', 'Data Analyst'),
('Nasser Al-Otaibi', 'alotaibi.n@northeastern.edu', 'MS_DS', 'Data Scientist'),
('Haruto Sato', 'sato.h@northeastern.edu', 'MS_DA', 'Data Analyst');

-- ============================================
-- STUDENT COURSES (realistic completed courses)
-- Each student has completed 2-5 courses
-- ============================================

INSERT INTO student_courses (student_id, course_code, completed_at, grade) VALUES
-- Aisha Patel (Data Engineer, MS_DAE)
(1, 'IE6400', '2025-05-15', 'A'),
(1, 'IE6700', '2025-05-15', 'A-'),
(1, 'IE6200', '2025-05-15', 'B+'),

-- Carlos Mendez (Data Scientist, MS_DAE)
(2, 'IE6400', '2025-05-15', 'A-'),
(2, 'IE7275', '2025-08-20', 'B+'),
(2, 'IE6600', '2025-08-20', 'A'),

-- Wei Zhang (Software Engineer, MS_CS)
(3, 'CS5800', '2025-05-15', 'A'),
(3, 'CS6140', '2025-08-20', 'A-'),

-- Priya Sharma (Data Analyst, MS_DAE)
(4, 'IE6400', '2025-05-15', 'B+'),
(4, 'IE6600', '2025-05-15', 'A-'),
(4, 'IE6200', '2025-08-20', 'B'),

-- James O'Brien (Data Scientist, MS_DS)
(5, 'DS5110', '2025-05-15', 'A'),
(5, 'DS5220', '2025-08-20', 'A-'),
(5, 'CS6140', '2025-08-20', 'B+'),

-- Fatima Al-Hassan (Data Engineer, MS_DAE)
(6, 'IE6400', '2025-05-15', 'A'),
(6, 'IE6700', '2025-08-20', 'A'),
(6, 'IE6200', '2025-05-15', 'A-'),
(6, 'IE6750', '2025-12-15', 'B+'),

-- Raj Krishnamurthy (Data Scientist, MS_CS)
(7, 'CS5800', '2025-05-15', 'A-'),
(7, 'CS6140', '2025-08-20', 'A'),
(7, 'CS6220', '2025-12-15', 'B+'),

-- Sofia Rossi (Business Analyst, MS_DA)
(8, 'DA5020', '2025-05-15', 'B+'),
(8, 'DA5030', '2025-08-20', 'B'),

-- Ahmed Khalil (Data Engineer, MS_DAE)
(9, 'IE6400', '2025-05-15', 'A-'),
(9, 'IE6700', '2025-08-20', 'B+'),

-- Emma Thompson (Data Scientist, MS_DS)
(10, 'DS5110', '2025-05-15', 'A'),
(10, 'DS5220', '2025-08-20', 'A'),
(10, 'DS5230', '2025-12-15', 'A-'),

-- Yuki Tanaka (Software Engineer, MS_CS)
(11, 'CS5800', '2025-05-15', 'A'),
(11, 'CS6140', '2025-08-20', 'A-'),
(11, 'CS7150', '2025-12-15', 'B+'),

-- Maria Santos (Data Analyst, MS_DA)
(12, 'DA5020', '2025-05-15', 'A-'),
(12, 'DA5030', '2025-08-20', 'B+'),

-- Kevin Park (Data Engineer, MS_DAE)
(13, 'IE6400', '2025-05-15', 'B+'),
(13, 'IE6200', '2025-05-15', 'A-'),
(13, 'IE6700', '2025-08-20', 'A'),
(13, 'IE6750', '2025-12-15', 'A-'),

-- Nia Johnson (Data Scientist, MS_DS)
(14, 'DS5110', '2025-05-15', 'A-'),
(14, 'DS5220', '2025-08-20', 'B+'),

-- Arjun Nair (Data Analyst, MS_DAE)
(15, 'IE6400', '2025-05-15', 'A'),
(15, 'IE6600', '2025-08-20', 'A-'),
(15, 'IE6200', '2025-08-20', 'B+'),

-- Isabella Ferreira (Business Analyst, MS_DA)
(16, 'DA5020', '2025-05-15', 'B'),
(16, 'DAMG6210', '2025-08-20', 'B+'),

-- Mohammed Rahman (Software Engineer, MS_CS)
(17, 'CS5800', '2025-05-15', 'A-'),
(17, 'CS6140', '2025-08-20', 'B+'),

-- Lin Chen (Data Engineer, MS_DAE)
(18, 'IE6400', '2025-05-15', 'A'),
(18, 'IE6700', '2025-05-15', 'A-'),
(18, 'IE6200', '2025-08-20', 'A'),
(18, 'IE7275', '2025-08-20', 'B+'),
(18, 'IE6750', '2025-12-15', 'A-'),

-- Zara Ahmed (Data Scientist, MS_DS)
(19, 'DS5110', '2025-05-15', 'A-'),
(19, 'CS6140', '2025-08-20', 'A'),

-- Lucas Silva (Data Analyst, MS_DA)
(20, 'DA5020', '2025-05-15', 'B+'),
(20, 'DA5030', '2025-08-20', 'A-'),

-- remaining students with 2-3 courses each
(21, 'IE6400', '2025-05-15', 'A'), (21, 'IE7275', '2025-08-20', 'B+'),
(22, 'CS5800', '2025-05-15', 'A-'), (22, 'CS6140', '2025-08-20', 'A'),
(23, 'IE6400', '2025-05-15', 'B+'), (23, 'IE6700', '2025-08-20', 'A-'),
(24, 'DS5110', '2025-05-15', 'A'), (24, 'DS5220', '2025-08-20', 'A-'),
(25, 'IE6400', '2025-05-15', 'A-'), (25, 'IE6600', '2025-08-20', 'B+'),
(26, 'DA5020', '2025-05-15', 'B+'), (26, 'DAMG6210', '2025-08-20', 'A-'),
(27, 'CS5800', '2025-05-15', 'A'), (27, 'CS6140', '2025-08-20', 'B+'),
(28, 'IE6400', '2025-05-15', 'A-'), (28, 'IE6700', '2025-08-20', 'A'),
(29, 'DS5110', '2025-05-15', 'B+'), (29, 'CS6140', '2025-08-20', 'A-'),
(30, 'DA5020', '2025-05-15', 'A-'), (30, 'DA5030', '2025-08-20', 'B+'),
(31, 'IE6400', '2025-05-15', 'A'), (31, 'IE6700', '2025-08-20', 'A-'), (31, 'IE6750', '2025-12-15', 'B+'),
(32, 'CS5800', '2025-05-15', 'B+'), (32, 'CS6140', '2025-08-20', 'A'),
(33, 'IE6400', '2025-05-15', 'A-'), (33, 'IE7275', '2025-08-20', 'A'),
(34, 'DS5110', '2025-05-15', 'A'), (34, 'DS5220', '2025-08-20', 'B+'), (34, 'DS5230', '2025-12-15', 'A-'),
(35, 'IE6400', '2025-05-15', 'B+'), (35, 'IE6700', '2025-08-20', 'A-'),
(36, 'DA5020', '2025-05-15', 'A-'), (36, 'DA5030', '2025-08-20', 'B'),
(37, 'CS5800', '2025-05-15', 'A'), (37, 'CS6140', '2025-08-20', 'A-'),
(38, 'IE6400', '2025-05-15', 'B+'), (38, 'IE6600', '2025-08-20', 'A'),
(39, 'DS5110', '2025-05-15', 'A-'), (39, 'DS5220', '2025-08-20', 'A'),
(40, 'DA5020', '2025-05-15', 'B'), (40, 'DA5030', '2025-08-20', 'B+'),
(41, 'IE6400', '2025-05-15', 'A'), (41, 'IE6700', '2025-08-20', 'A'), (41, 'IE6200', '2025-08-20', 'A-'),
(42, 'CS5800', '2025-05-15', 'A-'), (42, 'CS6140', '2025-08-20', 'B+'),
(43, 'IE6400', '2025-05-15', 'A'), (43, 'IE7275', '2025-08-20', 'A-'),
(44, 'DS5110', '2025-05-15', 'B+'), (44, 'DS5220', '2025-08-20', 'A'),
(45, 'IE6400', '2025-05-15', 'A-'), (45, 'IE6700', '2025-08-20', 'B+'),
(46, 'DA5020', '2025-05-15', 'A'), (46, 'DAMG6210', '2025-08-20', 'A-'),
(47, 'CS5800', '2025-05-15', 'B+'), (47, 'CS6140', '2025-08-20', 'A'),
(48, 'IE6400', '2025-05-15', 'A-'), (48, 'IE6600', '2025-08-20', 'B+'),
(49, 'DS5110', '2025-05-15', 'A'), (49, 'CS6140', '2025-08-20', 'A-'),
(50, 'DA5020', '2025-05-15', 'B+'), (50, 'DA5030', '2025-08-20', 'A-'),
(51, 'IE6400', '2025-05-15', 'A'), (51, 'IE6700', '2025-08-20', 'A-'), (51, 'IE6200', '2025-08-20', 'B+'),
(52, 'CS5800', '2025-05-15', 'A-'), (52, 'CS6140', '2025-08-20', 'A'),
(53, 'IE6400', '2025-05-15', 'B+'), (53, 'IE7275', '2025-08-20', 'A-'),
(54, 'DS5110', '2025-05-15', 'A'), (54, 'DS5220', '2025-08-20', 'A'), (54, 'DS5230', '2025-12-15', 'B+'),
(55, 'IE6400', '2025-05-15', 'A-'), (55, 'IE6700', '2025-08-20', 'A'),
(56, 'DA5020', '2025-05-15', 'B'), (56, 'DA5030', '2025-08-20', 'B+'),
(57, 'CS5800', '2025-05-15', 'A'), (57, 'CS6140', '2025-08-20', 'A-'),
(58, 'IE6400', '2025-05-15', 'B+'), (58, 'IE6600', '2025-08-20', 'A'),
(59, 'DS5110', '2025-05-15', 'A-'), (59, 'DS5220', '2025-08-20', 'B+'),
(60, 'DA5020', '2025-05-15', 'A-'), (60, 'DA5030', '2025-08-20', 'A'),
(61, 'IE6400', '2025-05-15', 'A'), (61, 'IE6700', '2025-08-20', 'A-'), (61, 'IE6750', '2025-12-15', 'A'),
(62, 'CS5800', '2025-05-15', 'B+'), (62, 'CS6140', '2025-08-20', 'A-'),
(63, 'IE6400', '2025-05-15', 'A-'), (63, 'IE7275', '2025-08-20', 'B+'),
(64, 'DS5110', '2025-05-15', 'A'), (64, 'DS5220', '2025-08-20', 'A-'),
(65, 'IE6400', '2025-05-15', 'B+'), (65, 'IE6700', '2025-08-20', 'A'),
(66, 'DA5020', '2025-05-15', 'A'), (66, 'DAMG6210', '2025-08-20', 'B+'),
(67, 'CS5800', '2025-05-15', 'A-'), (67, 'CS6140', '2025-08-20', 'A'),
(68, 'IE6400', '2025-05-15', 'A'), (68, 'IE6600', '2025-08-20', 'A-'),
(69, 'DS5110', '2025-05-15', 'B+'), (69, 'CS6140', '2025-08-20', 'A'),
(70, 'DA5020', '2025-05-15', 'A-'), (70, 'DA5030', '2025-08-20', 'B+'),
(71, 'IE6400', '2025-05-15', 'A'), (71, 'IE6700', '2025-08-20', 'A'), (71, 'IE6200', '2025-08-20', 'A'),
(72, 'CS5800', '2025-05-15', 'A-'), (72, 'CS6140', '2025-08-20', 'B+'),
(73, 'IE6400', '2025-05-15', 'B+'), (73, 'IE7275', '2025-08-20', 'A-'),
(74, 'DS5110', '2025-05-15', 'A'), (74, 'DS5220', '2025-08-20', 'A'), (74, 'DS5230', '2025-12-15', 'A-'),
(75, 'IE6400', '2025-05-15', 'A-'), (75, 'IE6700', '2025-08-20', 'B+'),
(76, 'DA5020', '2025-05-15', 'B+'), (76, 'DA5030', '2025-08-20', 'A-'),
(77, 'CS5800', '2025-05-15', 'A'), (77, 'CS6140', '2025-08-20', 'A'),
(78, 'IE6400', '2025-05-15', 'A-'), (78, 'IE6600', '2025-08-20', 'A'),
(79, 'DS5110', '2025-05-15', 'A'), (79, 'DS5220', '2025-08-20', 'A-'),
(80, 'DA5020', '2025-05-15', 'B'), (80, 'DA5030', '2025-08-20', 'B+'),
(81, 'IE6400', '2025-05-15', 'A'), (81, 'IE6700', '2025-08-20', 'A-'), (81, 'IE6750', '2025-12-15', 'B+'),
(82, 'CS5800', '2025-05-15', 'B+'), (82, 'CS6140', '2025-08-20', 'A'),
(83, 'IE6400', '2025-05-15', 'A-'), (83, 'IE7275', '2025-08-20', 'A'),
(84, 'DS5110', '2025-05-15', 'B+'), (84, 'DS5220', '2025-08-20', 'A-'),
(85, 'IE6400', '2025-05-15', 'A'), (85, 'IE6700', '2025-08-20', 'A'),
(86, 'DA5020', '2025-05-15', 'A-'), (86, 'DAMG6210', '2025-08-20', 'A'),
(87, 'CS5800', '2025-05-15', 'A'), (87, 'CS6140', '2025-08-20', 'A-'),
(88, 'IE6400', '2025-05-15', 'B+'), (88, 'IE6600', '2025-08-20', 'A-'),
(89, 'DS5110', '2025-05-15', 'A-'), (89, 'CS6140', '2025-08-20', 'B+'),
(90, 'DA5020', '2025-05-15', 'A'), (90, 'DA5030', '2025-08-20', 'A-'),
(91, 'IE6400', '2025-05-15', 'A'), (91, 'IE6700', '2025-08-20', 'A'), (91, 'IE6200', '2025-08-20', 'B+'),
(92, 'CS5800', '2025-05-15', 'A-'), (92, 'CS6140', '2025-08-20', 'A'),
(93, 'IE6400', '2025-05-15', 'B+'), (93, 'IE7275', '2025-08-20', 'A-'),
(94, 'DS5110', '2025-05-15', 'A'), (94, 'DS5220', '2025-08-20', 'A'), (94, 'DS5230', '2025-12-15', 'B+'),
(95, 'IE6400', '2025-05-15', 'A-'), (95, 'IE6700', '2025-08-20', 'B+'),
(96, 'DA5020', '2025-05-15', 'B+'), (96, 'DA5030', '2025-08-20', 'A'),
(97, 'CS5800', '2025-05-15', 'A'), (97, 'CS6140', '2025-08-20', 'A-'),
(98, 'IE6400', '2025-05-15', 'A-'), (98, 'IE6600', '2025-08-20', 'A'),
(99, 'DS5110', '2025-05-15', 'A'), (99, 'DS5220', '2025-08-20', 'B+'),
(100, 'DA5020', '2025-05-15', 'A-'), (100, 'DA5030', '2025-08-20', 'A');