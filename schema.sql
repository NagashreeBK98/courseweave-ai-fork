

-- ============================================
-- COURSE METADATA
-- ============================================

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    course_code VARCHAR(20) UNIQUE NOT NULL,   -- IE7275
    course_name TEXT NOT NULL,
    credits INTEGER NOT NULL,
    program_code VARCHAR(20) NOT NULL,         -- MS_DAE, MS_CS
    course_type VARCHAR(20) NOT NULL,          -- Core, Elective
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW()
);


CREATE TABLE prerequisites (
    id SERIAL PRIMARY KEY,
    course_code VARCHAR(20) NOT NULL REFERENCES courses(course_code),
    required_course_code VARCHAR(20) NOT NULL REFERENCES courses(course_code),
    UNIQUE(course_code, required_course_code)
);

-- ============================================
-- USER STATE
-- ============================================

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    program_code VARCHAR(20) NOT NULL,         -- MS_DAE, MS_CS
    target_career VARCHAR(100),                -- Data Engineer, Data Scientist
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE student_courses (
    id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL REFERENCES students(id),
    course_code VARCHAR(20) NOT NULL REFERENCES courses(course_code),
    completed_at DATE NOT NULL,
    grade VARCHAR(5),
    UNIQUE(student_id, course_code)
);