import streamlit as st

def home_page():
    st.markdown(
        """
        <style>
            /* Base Styles and Typography */
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

            .stApp {
                background-color: #1a1a2e;
                color: #e0e0e0;
                font-family: 'Poppins', sans-serif;
            }

            .st-emotion-cache-1wv7cff {
                background-color: #0f0f1d;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
                position: sticky;
                top: 0;
                z-index: 1000;
            }

            a {
                text-decoration: none;
                color: inherit;
            }

            h1 {
                font-weight: 700;
                color: #ffffff;
                font-size: 2.5rem;
                line-height: 1.2;
                margin-bottom: 2rem;
                max-width: 800px;
            }

            /* Header and Navigation */
            .header-container {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 1rem 5%;
            }

            .logo-container {
                display: flex;
                align-items: center;
                gap: 1rem;
            }

            .logo-image {
                width: 40px;
                height: 40px;
                object-fit: contain;
            }

            .logo-text {
                font-size: 1.5rem;
                font-weight: 700;
                color: #6a82fb;
            }

            .main-nav ul {
                list-style: none;
                display: flex;
                margin: 0;
                padding: 0;
                gap: 2rem;
            }

            .main-nav a {
                font-weight: 500;
                color: #e0e0e0;
                transition: color 0.3s ease;
            }

            .main-nav a:hover {
                color: #6a82fb;
            }

            .login-link {
                display: none;
            }

            /* Announcement Banner */
            .announcement-banner {
                background-color: #6a82fb;
                color: #ffffff;
                text-align: center;
                padding: 0.75rem;
                font-size: 0.9rem;
            }

            .new-tag {
                background-color: #ff6b6b;
                color: #ffffff;
                padding: 0.2rem 0.6rem;
                border-radius: 12px;
                font-weight: 600;
                margin-right: 0.5rem;
            }

            .announcement-banner a {
                text-decoration: underline;
                font-weight: 600;
                color: #ffffff;
            }

            /* Hero Section and Course Cards */
            .hero-section {
                display: flex;
                flex-direction: column;
                align-items: center;
                text-align: center;
                padding: 4rem 5%;
            }

            .course-cards-container {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 2rem;
                margin-top: 2rem;
                margin-bottom: 2rem;
            }

            .course-card {
                background-color: #2c2c3e;
                border-radius: 12px;
                box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
                overflow: hidden;
                max-width: 320px;
                transition: transform 0.3s ease;
            }

            .course-card:hover {
                transform: translateY(-10px);
            }

            .course-card img {
                width: 100%;
                height: 200px;
                object-fit: cover;
                display: block;
            }

            .course-info {
                padding: 1.5rem;
                position: relative;
                text-align: left;
            }

            .course-info h2 {
                font-size: 1.25rem;
                font-weight: 600;
                color: #ffffff;
                margin: 0 0 1rem 0;
            }

            .course-person {
                width: 80px;
                height: 80px;
                border-radius: 50%;
                position: absolute;
                top: -50px;
                right: 1.5rem;
                border: 4px solid #1a1a2e;
            }

            /* Google Form Button Styles */
            .google-form-btn-container {
                text-align: center;
                margin-top: 2rem;
                margin-bottom: 4rem;
            }

            .google-form-btn {
                display: inline-block;
                background-color: #6a82fb;
                color: #fff;
                padding: 1rem 2.5rem;
                border-radius: 8px;
                font-size: 1.1rem;
                font-weight: 600;
                transition: background-color 0.3s ease, transform 0.3s ease;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
            }

            .google-form-btn:hover {
                background-color: #4f67d4;
                transform: translateY(-2px);
            }
        </style>

        <header class="main-header">
            <div class="header-container">
                <div class="logo-container">
                    <img src="https://via.placeholder.com/40x40.png" alt="Codevia Logo" class="logo-image">
                    <a href="index.html">
                        <span class="logo-text">Codevia</span>
                    </a>
                </div>
                <nav class="main-nav">
                    <ul>
                        <li><a href="#" onclick="set_page('home')">Home</a></li>
                        <li><a href="#" onclick="set_page('programs')">Programs</a></li>
                        <li><a href="https://forms.gle/ZW49LUFnoQzMfkdS6" target="_blank">Contact</a></li>
                    </ul>
                </nav>
            </div>
        </header>

        <div class="announcement-banner">
            <p>
                <span class="new-tag">Loot</span>20% off with Student Id Proof <a href="YOUR_GOOGLE_FORM_URL_HERE">Know more →</a>
            </p>
        </div>

        <main class="hero-section">
            <div class="hero-content">
                <h1>Learn the syntax in live</h1>
                <div class="course-cards-container">
                    <div class="course-card">
                        <a href="#" onclick="set_page('python15days')">
                            <img src="https://via.placeholder.com/320x200.png" alt="Python 15-day Program">
                            <div class="course-info">
                                <h2>Python 15-day Program</h2>
                                <img class="course-person" src="https://via.placeholder.com/100x100.png?text=Student" alt="Student 1">
                            </div>
                        </a>
                    </div>
                    <div class="course-card">
                        <a href="#" onclick="set_page('python30days')">
                            <img src="https://via.placeholder.com/320x200.png" alt="Python 30-day Program">
                            <div class="course-info">
                                <h2>Python 30-day Program</h2>
                                <img class="course-person" src="https://via.placeholder.com/100x100.png?text=Student" alt="Student 2">
                            </div>
                        </a>
                    </div>
                    <div class="course-card">
                        <a href="#" onclick="set_page('sql')">
                            <img src="https://via.placeholder.com/320x200.png" alt="Project, SQL, and RDBMS with Projects">
                            <div class="course-info">
                                <h2>Project, SQL, and RDBMS with Projects</h2>
                                <img class="course-person" src="https://via.placeholder.com/100x100.png?text=Student" alt="Student 3">
                            </div>
                        </a>
                    </div>
                </div>

                <div class="google-form-btn-container">
                    <a href="https://forms.gle/y6rxBFMBm86eYAtQA" class="google-form-btn" target="_blank">Register Here</a>
                </div>
            </div>
        </main>
        
        <footer class="main-footer">
            <p>&copy; 2025 Codevia. All Rights Reserved.</p>
        </footer>
        """,
        unsafe_allow_html=True
    )

def programs_page():
    st.markdown(
        """
        <style>
            /* Copied CSS from other pages */
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
            .stApp { background-color: #1a1a2e; color: #e0e0e0; font-family: 'Poppins', sans-serif; }
            a { text-decoration: none; color: inherit; }
            h1 { font-weight: 700; color: #ffffff; font-size: 2.5rem; line-height: 1.2; margin-bottom: 2rem; max-width: 800px; }
            .main-header { background-color: #0f0f1d; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); position: sticky; top: 0; z-index: 1000; }
            .header-container { display: flex; justify-content: space-between; align-items: center; padding: 1rem 5%; }
            .logo-text { font-size: 1.5rem; font-weight: 700; color: #6a82fb; }
            .main-nav ul { list-style: none; display: flex; margin: 0; padding: 0; gap: 2rem; }
            .main-nav a { font-weight: 500; color: #e0e0e0; transition: color 0.3s ease; }
            .main-nav a:hover { color: #6a82fb; }
            .login-link { display: none; }
            .announcement-banner { background-color: #6a82fb; color: #ffffff; text-align: center; padding: 0.75rem; font-size: 0.9rem; }
            .new-tag { background-color: #ff6b6b; color: #ffffff; padding: 0.2rem 0.6rem; border-radius: 12px; font-weight: 600; margin-right: 0.5rem; }
            .announcement-banner a { text-decoration: underline; font-weight: 600; color: #ffffff; }
            .hero-section { display: flex; flex-direction: column; align-items: center; text-align: center; padding: 4rem 5%; }
            .course-cards-container { display: flex; flex-wrap: wrap; justify-content: center; gap: 2rem; margin-top: 2rem; }
            .course-card { background-color: #2c2c3e; border-radius: 12px; box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); overflow: hidden; max-width: 320px; transition: transform 0.3s ease; }
            .course-card:hover { transform: translateY(-10px); }
            .course-card img { width: 100%; height: 200px; object-fit: cover; display: block; }
            .course-info { padding: 1.5rem; position: relative; text-align: left; }
            .course-info h2 { font-size: 1.25rem; font-weight: 600; color: #ffffff; margin: 0 0 1rem 0; }
            .course-person { width: 80px; height: 80px; border-radius: 50%; position: absolute; top: -50px; right: 1.5rem; border: 4px solid #1a1a2e; }
            .main-footer { text-align: center; padding: 2rem; background-color: #0f0f1d; border-top: 1px solid #2c2c3e; font-size: 0.9rem; color: #999; }
            @media (max-width: 768px) { .header-container { flex-direction: column; gap: 1rem; } .main-nav ul { flex-direction: column; align-items: center; gap: 1rem; } h1 { font-size: 2rem; } }
        </style>
        
        <header class="main-header">
            <div class="header-container">
                <div class="logo">
                    <a href="#" onclick="set_page('home')">
                        <span class="logo-text">Codevia</span>
                    </a>
                </div>
                <nav class="main-nav">
                    <ul>
                        <li><a href="#" onclick="set_page('home')">Home</a></li>
                        <li><a href="#" onclick="set_page('programs')">Programs</a></li>
                        <li><a href="https://forms.gle/ZW49LUFnoQzMfkdS6" target="_blank">Contact</a></li>
                    </ul>
                </nav>
            </div>
        </header>

        <main class="hero-section" style="padding: 2rem 5%;">
            <div class="hero-content" style="max-width: 100%;">
                <h1>Our Programs</h1>
                <p style="color: #999; font-size: 1.1rem; max-width: 700px; margin: 0 auto 3rem;">Explore our range of comprehensive programs designed to turn you into a pro.</p>
                <div class="course-cards-container">
                    <div class="course-card">
                        <a href="#" onclick="set_page('python15days')">
                            <img src="https://via.placeholder.com/300x200.png?text=Python+15+Days" alt="Python 15-day Program">
                            <div class="course-info">
                                <h2>Python 15-day Program</h2>
                            </div>
                        </a>
                    </div>
                    <div class="course-card">
                        <a href="#" onclick="set_page('python30days')">
                            <img src="https://via.placeholder.com/300x200.png?text=Python+30+Days" alt="Python 30-day Program">
                            <div class="course-info">
                                <h2>Python 30-day Program</h2>
                            </div>
                        </a>
                    </div>
                    <div class="course-card">
                        <a href="#" onclick="set_page('sql')">
                            <img src="https://via.placeholder.com/300x200.png?text=SQL+RDBMS+Projects" alt="Project, SQL, and RDBMS with Projects">
                            <div class="course-info">
                                <h2>Project, SQL, and RDBMS with Projects</h2>
                            </div>
                        </a>
                    </div>
                </div>
            </div>
        </main>
        
        <footer class="main-footer">
            <p>&copy; 2025 Codevia. All Rights Reserved.</p>
        </footer>
        """,
        unsafe_allow_html=True
    )

def python15days_page():
    st.markdown(
        """
        <style>
            /* Copied CSS from other pages */
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
            .stApp { background-color: #1a1a2e; color: #e0e0e0; font-family: 'Poppins', sans-serif; }
            a { text-decoration: none; color: inherit; }
            h1 { font-weight: 700; color: #ffffff; font-size: 2.5rem; line-height: 1.2; margin-bottom: 2rem; max-width: 800px; }
            .main-header { background-color: #0f0f1d; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); position: sticky; top: 0; z-index: 1000; }
            .header-container { display: flex; justify-content: space-between; align-items: center; padding: 1rem 5%; }
            .logo-text { font-size: 1.5rem; font-weight: 700; color: #6a82fb; }
            .main-nav ul { list-style: none; display: flex; margin: 0; padding: 0; gap: 2rem; }
            .main-nav a { font-weight: 500; color: #e0e0e0; transition: color 0.3s ease; }
            .main-nav a:hover { color: #6a82fb; }
            .login-link { display: none; }
            .announcement-banner { background-color: #6a82fb; color: #ffffff; text-align: center; padding: 0.75rem; font-size: 0.9rem; }
            .new-tag { background-color: #ff6b6b; color: #ffffff; padding: 0.2rem 0.6rem; border-radius: 12px; font-weight: 600; margin-right: 0.5rem; }
            .announcement-banner a { text-decoration: underline; font-weight: 600; color: #ffffff; }
            .hero-section { display: flex; flex-direction: column; align-items: center; text-align: center; padding: 4rem 5%; }
            .course-cards-container { display: flex; flex-wrap: wrap; justify-content: center; gap: 2rem; margin-top: 2rem; }
            .course-card { background-color: #2c2c3e; border-radius: 12px; box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); overflow: hidden; max-width: 320px; transition: transform 0.3s ease; }
            .course-card:hover { transform: translateY(-10px); }
            .course-card img { width: 100%; height: 200px; object-fit: cover; display: block; }
            .course-info { padding: 1.5rem; position: relative; text-align: left; }
            .course-info h2 { font-size: 1.25rem; font-weight: 600; color: #ffffff; margin: 0 0 1rem 0; }
            .course-person { width: 80px; height: 80px; border-radius: 50%; position: absolute; top: -50px; right: 1.5rem; border: 4px solid #1a1a2e; }
            .main-footer { text-align: center; padding: 2rem; background-color: #0f0f1d; border-top: 1px solid #2c2c3e; font-size: 0.9rem; color: #999; }
            @media (max-width: 768px) { .header-container { flex-direction: column; gap: 1rem; } .main-nav ul { flex-direction: column; align-items: center; gap: 1rem; } h1 { font-size: 2rem; } }
            
            /* Course Details Page Styles */
            .course-details-container { max-width: 800px; margin: 3rem auto; padding: 2rem; background-color: #2c2c3e; border-radius: 12px; box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); }
            .course-details-container h1 { text-align: center; }
            .course-details-container img { width: 100%; height: auto; border-radius: 12px; margin-bottom: 2rem; }
            .course-details-container p, .course-details-container ul { font-size: 1.1rem; line-height: 1.6; color: #e0e0e0; }
            .course-details-container ul { list-style-type: none; padding-left: 0; }
            .course-details-container ul li:before { content: "✓ "; color: #6a82fb; }
            .enroll-btn { display: inline-block; background-color: #6a82fb; color: #fff; padding: 1rem 2rem; border-radius: 8px; font-size: 1rem; font-weight: 600; margin-top: 2rem; transition: background-color 0.3s ease; }
            .enroll-btn:hover { background-color: #4f67d4; }
        </style>
        
        <header class="main-header">
            <div class="header-container">
                <div class="logo">
                    <a href="#" onclick="set_page('home')">
                        <span class="logo-text">Codevia</span>
                    </a>
                </div>
                <nav class="main-nav">
                    <ul>
                        <li><a href="#" onclick="set_page('home')">Home</a></li>
                        <li><a href="#" onclick="set_page('programs')">Programs</a></li>
                        <li><a href="https://forms.gle/ZW49LUFnoQzMfkdS6" target="_blank">Contact</a></li>
                    </ul>
                </nav>
            </div>
        </header>
        
        <main class="course-page">
            <div class="course-details-container">
                <h1>Python 15-day Program</h1>
                <img src="https://via.placeholder.com/800x450.png?text=Python+15-day+Program" alt="Python 15-day Program">
                <p>This intensive 15-day program is perfect for beginners who want to learn the fundamentals of Python quickly. You'll cover essential topics and build a solid foundation in programming.</p>
                <h3>What You'll Learn:</h3>
                <ul>
                    <li>Python Syntax and Basics</li>
                    <li>Data Types and Variables</li>
                    <li>Control Flow and Functions</li>
                    <li>Basic Data Structures (Lists, Dictionaries)</li>
                </ul>
                <a href="#" class="enroll-btn">Enroll Now</a>
            </div>
        </main>
        
        <footer class="main-footer">
            <p>&copy; 2025 Codevia. All Rights Reserved.</p>
        </footer>
        """,
        unsafe_allow_html=True
    )

def python30days_page():
    st.markdown(
        """
        <style>
            /* Copied CSS from other pages */
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
            .stApp { background-color: #1a1a2e; color: #e0e0e0; font-family: 'Poppins', sans-serif; }
            a { text-decoration: none; color: inherit; }
            h1 { font-weight: 700; color: #ffffff; font-size: 2.5rem; line-height: 1.2; margin-bottom: 2rem; max-width: 800px; }
            .main-header { background-color: #0f0f1d; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); position: sticky; top: 0; z-index: 1000; }
            .header-container { display: flex; justify-content: space-between; align-items: center; padding: 1rem 5%; }
            .logo-text { font-size: 1.5rem; font-weight: 700; color: #6a82fb; }
            .main-nav ul { list-style: none; display: flex; margin: 0; padding: 0; gap: 2rem; }
            .main-nav a { font-weight: 500; color: #e0e0e0; transition: color 0.3s ease; }
            .main-nav a:hover { color: #6a82fb; }
            .login-link { display: none; }
            .announcement-banner { background-color: #6a82fb; color: #ffffff; text-align: center; padding: 0.75rem; font-size: 0.9rem; }
            .new-tag { background-color: #ff6b6b; color: #ffffff; padding: 0.2rem 0.6rem; border-radius: 12px; font-weight: 600; margin-right: 0.5rem; }
            .announcement-banner a { text-decoration: underline; font-weight: 600; color: #ffffff; }
            .hero-section { display: flex; flex-direction: column; align-items: center; text-align: center; padding: 4rem 5%; }
            .course-cards-container { display: flex; flex-wrap: wrap; justify-content: center; gap: 2rem; margin-top: 2rem; }
            .course-card { background-color: #2c2c3e; border-radius: 12px; box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); overflow: hidden; max-width: 320px; transition: transform 0.3s ease; }
            .course-card:hover { transform: translateY(-10px); }
            .course-card img { width: 100%; height: 200px; object-fit: cover; display: block; }
            .course-info { padding: 1.5rem; position: relative; text-align: left; }
            .course-info h2 { font-size: 1.25rem; font-weight: 600; color: #ffffff; margin: 0 0 1rem 0; }
            .course-person { width: 80px; height: 80px; border-radius: 50%; position: absolute; top: -50px; right: 1.5rem; border: 4px solid #1a1a2e; }
            .main-footer { text-align: center; padding: 2rem; background-color: #0f0f1d; border-top: 1px solid #2c2c3e; font-size: 0.9rem; color: #999; }
            @media (max-width: 768px) { .header-container { flex-direction: column; gap: 1rem; } .main-nav ul { flex-direction: column; align-items: center; gap: 1rem; } h1 { font-size: 2rem; } }
            
            /* Course Details Page Styles */
            .course-details-container { max-width: 800px; margin: 3rem auto; padding: 2rem; background-color: #2c2c3e; border-radius: 12px; box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); }
            .course-details-container h1 { text-align: center; }
            .course-details-container img { width: 100%; height: auto; border-radius: 12px; margin-bottom: 2rem; }
            .course-details-container p, .course-details-container ul { font-size: 1.1rem; line-height: 1.6; color: #e0e0e0; }
            .course-details-container ul { list-style-type: none; padding-left: 0; }
            .course-details-container ul li:before { content: "✓ "; color: #6a82fb; }
            .enroll-btn { display: inline-block; background-color: #6a82fb; color: #fff; padding: 1rem 2rem; border-radius: 8px; font-size: 1rem; font-weight: 600; margin-top: 2rem; transition: background-color 0.3s ease; }
            .enroll-btn:hover { background-color: #4f67d4; }
        </style>
        
        <header class="main-header">
            <div class="header-container">
                <div class="logo">
                    <a href="#" onclick="set_page('home')">
                        <span class="logo-text">Codevia</span>
                    </a>
                </div>
                <nav class="main-nav">
                    <ul>
                        <li><a href="#" onclick="set_page('home')">Home</a></li>
                        <li><a href="#" onclick="set_page('programs')">Programs</a></li>
                        <li><a href="https://forms.gle/ZW49LUFnoQzMfkdS6" target="_blank">Contact</a></li>
                    </ul>
                </nav>
            </div>
        </header>
        
        <main class="course-page">
            <div class="course-details-container">
                <h1>Python 30-day Program</h1>
                <img src="https://via.placeholder.com/800x450.png?text=Python+30-day+Program" alt="Python 30-day Program">
                <p>This 30-day program takes you from beginner to intermediate, diving deeper into Python concepts and best practices. You'll build more complex applications and gain practical experience.</p>
                <h3>What You'll Learn:</h3>
                <ul>
                    <li>Advanced Data Structures (Stacks, Queues)</li>
                    <li>Object-Oriented Programming (OOP)</li>
                    <li>File Handling and Modules</li>
                    <li>Introduction to Web Scraping</li>
                </ul>
                <a href="#" class="enroll-btn">Enroll Now</a>
            </div>
        </main>
        
        <footer class="main-footer">
            <p>&copy; 2025 Codevia. All Rights Reserved.</p>
        </footer>
        """,
        unsafe_allow_html=True
    )

def sql_page():
    st.markdown(
        """
        <style>
            /* Copied CSS from other pages */
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
            .stApp { background-color: #1a1a2e; color: #e0e0e0; font-family: 'Poppins', sans-serif; }
            a { text-decoration: none; color: inherit; }
            h1 { font-weight: 700; color: #ffffff; font-size: 2.5rem; line-height: 1.2; margin-bottom: 2rem; max-width: 800px; }
            .main-header { background-color: #0f0f1d; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); position: sticky; top: 0; z-index: 1000; }
            .header-container { display: flex; justify-content: space-between; align-items: center; padding: 1rem 5%; }
            .logo-text { font-size: 1.5rem; font-weight: 700; color: #6a82fb; }
            .main-nav ul { list-style: none; display: flex; margin: 0; padding: 0; gap: 2rem; }
            .main-nav a { font-weight: 500; color: #e0e0e0; transition: color 0.3s ease; }
            .main-nav a:hover { color: #6a82fb; }
            .login-link { display: none; }
            .announcement-banner { background-color: #6a82fb; color: #ffffff; text-align: center; padding: 0.75rem; font-size: 0.9rem; }
            .new-tag { background-color: #ff6b6b; color: #ffffff; padding: 0.2rem 0.6rem; border-radius: 12px; font-weight: 600; margin-right: 0.5rem; }
            .announcement-banner a { text-decoration: underline; font-weight: 600; color: #ffffff; }
            .hero-section { display: flex; flex-direction: column; align-items: center; text-align: center; padding: 4rem 5%; }
            .course-cards-container { display: flex; flex-wrap: wrap; justify-content: center; gap: 2rem; margin-top: 2rem; }
            .course-card { background-color: #2c2c3e; border-radius: 12px; box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); overflow: hidden; max-width: 320px; transition: transform 0.3s ease; }
            .course-card:hover { transform: translateY(-10px); }
            .course-card img { width: 100%; height: 200px; object-fit: cover; display: block; }
            .course-info { padding: 1.5rem; position: relative; text-align: left; }
            .course-info h2 { font-size: 1.25rem; font-weight: 600; color: #ffffff; margin: 0 0 1rem 0; }
            .course-person { width: 80px; height: 80px; border-radius: 50%; position: absolute; top: -50px; right: 1.5rem; border: 4px solid #1a1a2e; }
            .main-footer { text-align: center; padding: 2rem; background-color: #0f0f1d; border-top: 1px solid #2c2c3e; font-size: 0.9rem; color: #999; }
            @media (max-width: 768px) { .header-container { flex-direction: column; gap: 1rem; } .main-nav ul { flex-direction: column; align-items: center; gap: 1rem; } h1 { font-size: 2rem; } }
            
            /* Course Details Page Styles */
            .course-details-container { max-width: 800px; margin: 3rem auto; padding: 2rem; background-color: #2c2c3e; border-radius: 12px; box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); }
            .course-details-container h1 { text-align: center; }
            .course-details-container img { width: 100%; height: auto; border-radius: 12px; margin-bottom: 2rem; }
            .course-details-container p, .course-details-container ul { font-size: 1.1rem; line-height: 1.6; color: #e0e0e0; }
            .course-details-container ul { list-style-type: none; padding-left: 0; }
            .course-details-container ul li:before { content: "✓ "; color: #6a82fb; }
            .enroll-btn { display: inline-block; background-color: #6a82fb; color: #fff; padding: 1rem 2rem; border-radius: 8px; font-size: 1rem; font-weight: 600; margin-top: 2rem; transition: background-color 0.3s ease; }
            .enroll-btn:hover { background-color: #4f67d4; }
        </style>
        
        <header class="main-header">
            <div class="header-container">
                <div class="logo">
                    <a href="#" onclick="set_page('home')">
                        <span class="logo-text">Codevia</span>
                    </a>
                </div>
                <nav class="main-nav">
                    <ul>
                        <li><a href="#" onclick="set_page('home')">Home</a></li>
                        <li><a href="#" onclick="set_page('programs')">Programs</a></li>
                        <li><a href="https://forms.gle/ZW49LUFnoQzMfkdS6" target="_blank">Contact</a></li>
                    </ul>
                </nav>
            </div>
        </header>
        
        <main class="course-page">
            <div class="course-details-container">
                <h1>Project, SQL, and RDBMS with Projects</h1>
                <img src="https://via.placeholder.com/800x450.png?text=SQL+and+RDBMS+Projects" alt="Project, SQL, and RDBMS with Projects">
                <p>This program focuses on building practical skills in databases. You'll work on hands-on projects, master SQL queries, and understand the core principles of Relational Database Management Systems (RDBMS).</p>
                <h3>What You'll Learn:</h3>
                <ul>
                    <li>SQL Fundamentals and Advanced Queries</li>
                    <li>Database Design and Normalization</li>
                    <li>Connecting Databases to Projects</li>
                    <li>Building Real-world Applications</li>
                </ul>
                <a href="#" class="enroll-btn">Enroll Now</a>
            </div>
        </main>
        
        <footer class="main-footer">
            <p>&copy; 2025 Codevia. All Rights Reserved.</p>
        </footer>
        """,
        unsafe_allow_html=True
    )

def know_more_buildathon_page():
    st.markdown(
        """
        <style>
            /* Copied CSS from other pages */
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
            .stApp { background-color: #1a1a2e; color: #e0e0e0; font-family: 'Poppins', sans-serif; }
            a { text-decoration: none; color: inherit; }
            h1 { font-weight: 700; color: #ffffff; font-size: 2.5rem; line-height: 1.2; margin-bottom: 2rem; max-width: 800px; }
            .main-header { background-color: #0f0f1d; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); position: sticky; top: 0; z-index: 1000; }
            .header-container { display: flex; justify-content: space-between; align-items: center; padding: 1rem 5%; }
            .logo-text { font-size: 1.5rem; font-weight: 700; color: #6a82fb; }
            .main-nav ul { list-style: none; display: flex; margin: 0; padding: 0; gap: 2rem; }
            .main-nav a { font-weight: 500; color: #e0e0e0; transition: color 0.3s ease; }
            .main-nav a:hover { color: #6a82fb; }
            .login-link { display: none; }
            .announcement-banner { background-color: #6a82fb; color: #ffffff; text-align: center; padding: 0.75rem; font-size: 0.9rem; }
            .new-tag { background-color: #ff6b6b; color: #ffffff; padding: 0.2rem 0.6rem; border-radius: 12px; font-weight: 600; margin-right: 0.5rem; }
            .announcement-banner a { text-decoration: underline; font-weight: 600; color: #ffffff; }
            .hero-section { display: flex; flex-direction: column; align-items: center; text-align: center; padding: 4rem 5%; }
            .course-cards-container { display: flex; flex-wrap: wrap; justify-content: center; gap: 2rem; margin-top: 2rem; }
            .course-card { background-color: #2c2c3e; border-radius: 12px; box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); overflow: hidden; max-width: 320px; transition: transform 0.3s ease; }
            .course-card:hover { transform: translateY(-10px); }
            .course-card img { width: 100%; height: 200px; object-fit: cover; display: block; }
            .course-info { padding: 1.5rem; position: relative; text-align: left; }
            .course-info h2 { font-size: 1.25rem; font-weight: 600; color: #ffffff; margin: 0 0 1rem 0; }
            .main-footer { text-align: center; padding: 2rem; background-color: #0f0f1d; border-top: 1px solid #2c2c3e; font-size: 0.9rem; color: #999; }
            @media (max-width: 768px) { .header-container { flex-direction: column; gap: 1rem; } .main-nav ul { flex-direction: column; align-items: center; gap: 1rem; } h1 { font-size: 2rem; } }

            /* Event Page Styles */
            .event-container { max-width: 900px; margin: 3rem auto; padding: 2rem; background-color: #2c2c3e; border-radius: 12px; box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); text-align: center; }
            .event-container h2 { font-size: 2rem; color: #ffffff; margin-bottom: 1rem; }
            .event-container p { font-size: 1.1rem; line-height: 1.6; margin-bottom: 2rem; color: #e0e0e0; }
            .event-details { text-align: left; margin-bottom: 2rem; }
            .event-details ul { list-style-type: none; padding-left: 0; }
            .event-details ul li { margin-bottom: 1rem; font-size: 1rem; }
            .event-details ul li strong { color: #6a82fb; }
            .register-btn { display: inline-block; background-color: #6a82fb; color: #fff; padding: 1rem 2.5rem; border-radius: 8px; font-size: 1rem; font-weight: 600; transition: background-color 0.3s ease; }
            .register-btn:hover { background-color: #4f67d4; }
        </style>
        
        <header class="main-header">
            <div class="header-container">
                <div class="logo">
                    <a href="#" onclick="set_page('home')">
                        <span class="logo-text">Codevia</span>
                    </a>
                </div>
                <nav class="main-nav">
                    <ul>
                        <li><a href="#" onclick="set_page('home')">Home</a></li>
                        <li><a href="#" onclick="set_page('programs')">Programs</a></li>
                        <li><a href="https://forms.gle/ZW49LUFnoQzMfkdS6" target="_blank">Contact</a></li>
                    </ul>
                </nav>
            </div>
        </header>

        <main class="event-page">
            <div class="event-container">
                <h2>OpenAI Academy x Codevia Buildathon</h2>
                <p>Join India's biggest GenAI challenge for students and build the future with us. This is your opportunity to work on cutting-edge projects, learn from experts, and showcase your skills.</p>
                <div class="event-details">
                    <ul>
                        <li><strong>Who Can Participate:</strong> All students passionate about technology and AI.</li>
                        <li><strong>What You'll Do:</strong> Solve real-world problems using Generative AI models.</li>
                        <li><strong>Prizes:</strong> Win exciting prizes and get a chance to be mentored by industry leaders.</li>
                        <li><strong>Dates:</strong> Registrations open now! The challenge begins on [Date].</li>
                    </ul>
                </div>
                <a href="https://forms.gle/aTwjdAeRiGL5xDMN9" class="register-btn" target="_blank">Register Now</a>
            </div>
        </main>
        
        <footer class="main-footer">
            <p>&copy; 2025 Codevia. All Rights Reserved.</p>
        </footer>
        """,
        unsafe_allow_html=True
    )

def main():
    if 'page' not in st.session_state:
        st.session_state.page = 'home'

    if st.session_state.page == 'home':
        home_page()
    elif st.session_state.page == 'programs':
        programs_page()
    elif st.session_state.page == 'python15days':
        python15days_page()
    elif st.session_state.page == 'python30days':
        python30days_page()
    elif st.session_state.page == 'sql':
        sql_page()
    elif st.session_state.page == 'know-more-buildathon':
        know_more_buildathon_page()

    # The contact page content is no longer needed since it redirects to the form
    # It's better to keep the navigation link in the header as an external link

    st.markdown(
        """
        <script>
            function set_page(page_name) {
                const urlParams = new URLSearchParams(window.location.search);
                urlParams.set('page', page_name);
                window.location.search = urlParams.toString();
            }
        </script>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()