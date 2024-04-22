import streamlit as st
import pandas as pd
from joblib import load




# -- Set page config
apptitle = 'DT2 & Obesity'

st.set_page_config(page_title=apptitle, 
                   page_icon="⚕️",
                   initial_sidebar_state='collapsed')


# Function to initialize session state
def init_session_state():
    return st.session_state.setdefault('selected_page', 'Home')

          
def page_home():
    st.write('36105 iLab: Capstone Project - Autumn 2024 - UTS')
    # Title
    st.title('How lifestyle/habits can lead to obesity and diabetes type 2')
    
    st.header('Research Question')
    st.markdown("""
    How do lifestyle factors and habits lead to obesity and type 2 diabetes and which one is the strongest predictive values?
    1. Examine the role of socio-economic status in lifestyle choices and its subsequent impact on health outcomes.
    2. Investigate specific lifestyle factors (diet, physical activity, sleep patterns, etc.) and their correlation with obesity and diabetes incidence.
    """)

    

def page_survey():
    """Displays the survey page title and introductory text with flexbox and adjusted markdown."""

    # Title
    font_family = "Copperplate, Fantasy"  

    text = f"""
<h1 style='text-align: center; color: #008080; font-size: 63px; font-family: {font_family}; font-weight: bolder'>
  Unlock Your Health Insights: Take Our Personalized Survey
</h1>
"""

    st.markdown(text, unsafe_allow_html=True)
    #st.markdown("<h1 style='text-align: center; color: #008080; font-size: 60px'; font-family: Papyrus, Fantasy'> Unlock Your Health Insights: Take Our Personalized Survey</h1>", unsafe_allow_html=True)


    # Subheader
    text2 = """
<h1 style='text-align: center; color: #2F4F4F; font-style: italic; font-size: 25px; font-family: Times New Roman, sans-serif;'>
  Help us get a quick snapshot of your health and well-being by answering a few quick questions!
</h1>
"""
    st.markdown(text2, unsafe_allow_html=True)
    #st.markdown("<h1 style='text-align: center; color: black; font-style: italic; font-size: 20px'>Help us get a quick snapshot of your health and well-being by answering a few quick questions!</h1>", unsafe_allow_html=True)


    st.divider()

    st.header('Tell us about yourself')

    gender = st.radio('Select your gender:',['Male','Female','I prefer not to say'])
    st.markdown(
    """<style>
div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 18px;
}
    </style>
    """, unsafe_allow_html=True)


    age = st.slider('Please select your age:', min_value=0, max_value=90, step=1)
    st.markdown(
    """<style>
div[class*="Slider"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 18px;
}
    </style>
    """, unsafe_allow_html=True)
    
    
    # Calculate BMI with user inputted height and weight (in metric)
    height = st.number_input('Please enter your height in cm:', min_value = 0.0, max_value = 250.0)
    weight = st.number_input('Please enter your weight in kg', min_value = 0.0, max_value = 300.0)
    st.markdown(
    """<style>
div[class*="NumberInput"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 18px;
}
    </style>
    """, unsafe_allow_html=True)
    
    

    # Calculate BMI
    height_in_ms = height/100
    
    if st.button('Calculate BMI') :
        if height != 0:
            bmi = round((weight / (height_in_ms ** 2)), 1)
            # df of WHO nutritional status by weight
            bmi_categories = {"Underweight": [0.0, 18.49], "Normal weight": [18.5, 24.9], "Pre-obesity": [25.0, 29.9], 
                                "Obesity class II":[35.0, 39.9], "Obesity class III": [40.0, 100]}
            bmi_df = pd.DataFrame(bmi_categories, index = ['Minimum Weight', 'Maximum Weight'])
            st.write("Your BMI is: ", bmi)
            st.write(bmi_df)
        elif height == None or weight == None:
            st.write('Please input height and weight')
        elif height == 0:
            st.write('Entered height cannot be 0. Please enter again')

    
    st.divider()

    st.header('Tell us about your health status')
    
    
    high_bp = st.radio('Do you have high blood pressure?',['Yes','No'])
    high_col = st.radio('Have you checked your cholesterol level in the last 5 years?',['Yes','No'])
    

    gen_health = st.radio('What would you say your health status is in general?',['Excellent','Very good','Good', 'Fair', 'Poor'])

    info3 = "Mental health includes stress, depression, and all problems connected with emotions etc."  
    men_health = st.slider("How many days in the past 30 days did you feel metnally unwell?", max_value=30)
    # HTML box
    st.markdown(f'<span title="{info3}"> ⓘ </span>', unsafe_allow_html=True)

    
    info4 = "Physical health includes all types of physical injuries and illnesses."
    phys_health = st.slider("How many days in the past 30 days did you feel physically unwell?", max_value=30)
    # HTML box
    st.markdown(f'<span title="{info4}"> ⓘ </span>', unsafe_allow_html=True)

    walk = st.radio('Do you have a serious difficulty walking or climbing stairs?',['Yes','No'])

    st.divider()

    st.header('Tell us about your education and income')

    st.radio('Your educational level:', ['Never attended school or only kindergarten',
                                         'Elementary',
                                         'High school dropout',
                                         'High school graduate',
                                         'Colleug or technical school dropout',
                                         'College graduate or above'])
    
    st.radio('Your annual income range:', ['[1 - 22,500]',
                                           '[22,501 - 33,750]',
                                           '[33,751 - 45,000]',
                                           '[45,001 - 52,500]',
                                           '[52,501 - 67,500]',
                                           '[67,501 - 75,000]'])
    st.info('st.info test')


def page_results(preds_val_xgb):

    col1, col2 = st.columns(2)

    if preds_val_xgb > 0:
        col1.button("Learn More about Obesity")
        col1.header("You do not need to go to the gym")
        col1.subheader("What do I write here")
        col1.write(f"This is the text box, the value from model is {preds_val_xgb}")
        col2.title("You're not diabetec")
        col2.header("This is result 2")
        col2.subheader("This is result 2 subheader")
        col2.write("This is text in the second box")
    else:
        tab1, tab2 = st.tabs(["Learn More about Obesity", "Learn More about Diabetes"])
        with tab1:
            page_facts_obesity()
            if st.button("Support and Resources for Obesity"):
                st.title("heeh")
        with tab2:
            page_facts_diabetes()
            if st.button("Support and Resources for Diabetes Type 2"):
                st.title("heeh")


def page_facts_obesity():
    st.markdown("<h1 style='text-align: center; color: #2A4258; font-family: American Typewriter, serif; font-weight: bold; font-size: 40px'>Facts about obesity that you should be aware of</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: left; font-family: Times New Roman, serif; font-weight: bold; font-size: 25px'>Understanding Obesity</h1>", unsafe_allow_html=True)
    st.markdown("""<h2 style='text-align: justify; font-size: 20px; font-family: Times New Roman; font-weight: normal'><b>Definition:</b> Obesity is a medical condition characterised by an excessive amount of body fat, which poses a risk to health. The World Health Organization (WHO) identifies obesity as a leading preventable cause of death worldwide, impacting life expectancy negatively and increasing the incidence of health problems. (Source: WHO)</h2>""", unsafe_allow_html=True)

    st.markdown("""<h2 style='text-align: justify; font-size: 20px; font-family: Times New Roman; font-weight: normal'><b>BMI Classifications:</b> The Body Mass Index (BMI) is a key metric used by the WHO to classify weight categories. It divides weight status into four main categories: underweight (BMI less than 18.5), normal weight (BMI 18.5 to <25), overweight (BMI 25 to <30), and obese (BMI 30 or higher). Obesity is further subdivided into classes: Class I (BMI 30 to <35), Class II (BMI 35 to <40), and Class III (BMI 40 or higher), with the latter also known as "severe" or "morbid" obesity. (Source: CDC)</h2>""", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: left; font-family: Times New Roman, serif; font-weight: bold; font-size: 25px'>Causes of Obesity</h1>", unsafe_allow_html=True)
    st.markdown("""<ul>
        <li><b>Diet:</b> The consumption of high-calorie foods, particularly those rich in sugars and fats, combined with large portion sizes, significantly contributes to the development of obesity. A diet that exceeds energy needs without sufficient physical activity leads to fat accumulation. (Sources: CDC, Mayo Clinic)</li>
        <li><b>Physical Inactivity:</b> A sedentary lifestyle, characterised by minimal physical activity, directly contributes to weight gain. Modern conveniences and technology have reduced the need for physical exertion in daily life, contributing to the obesity epidemic. (Sources: CDC, Mayo Clinic)</li>
        <li><b>Genetics:</b> Genetic predisposition plays a significant role in obesity. Individuals with a family history of obesity are at a higher risk, as genetics can influence fat storage and energy metabolism. (Sources: CDC, Mayo Clinic)</li>
        <li><b>Psychological Factors:</b> Emotional states such as stress and depression can lead to overeating as a coping mechanism, contributing to obesity. The relationship between emotions and eating behaviour is complex and multifaceted. (Sources: CDC, Mayo Clinic)</li>
        <li><b>Environmental Factors:</b> The environment, including access to healthy foods and safe areas for exercise, significantly affects lifestyle choices and obesity risk. Socioeconomic factors can influence diet and physical activity levels. (Sources: CDC, Mayo Clinic)</li>
        <li><b>Medicines:</b> Certain medications can lead to weight gain by altering the body's energy balance or increasing appetite. Medications for diabetes, depression, and high blood pressure are examples of those that can affect weight. (Source: NHLBI)</li>
        </ul>""", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: left; font-family: Times New Roman, serif; font-weight: bold; font-size: 25px'>Health Risks Associated with Obesity</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: justify; font-size: 20px; font-family: Times New Roman; font-weight: normal'>Obesity significantly increases the risk for numerous health conditions that can affect nearly every system in the body:</h2>", unsafe_allow_html=True)
    st.markdown("""<ul>
        <li><b>Cardiovascular Diseases:</b> Obesity contributes to heart disease and strokes, mainly through high blood pressure and abnormal cholesterol levels, posing serious risks to heart health. (Sources: Mayo Clinic, CDC)</li>
        <li><b>Metabolic Disorders:</b> Conditions such as type 2 diabetes and insulin resistance are closely linked to obesity, as excess body fat affects the body's ability to use insulin, leading to elevated blood sugar levels. (Sources: Mayo Clinic, NIDDK)</li>
        <li><b>Cancer:</b> There's a heightened risk for several types of cancer, including uterine, breast, colon, and liver cancer, among others, associated with obesity. (Sources: Mayo Clinic, CDC)</li>
        <li><b>Digestive Issues:</b> Obesity increases the likelihood of experiencing digestive problems like heartburn, gallbladder disease, and serious liver conditions, including fatty liver disease. (Sources: Mayo Clinic, CDC)</li>
        <li><b>Respiratory Problems:</b> Excess weight is a key factor in the development of sleep apnea and can contribute to other respiratory issues, impacting overall respiratory health. (Sources: Mayo Clinic, CDC)</li>
        <li><b>Joint and Inflammation Issues:</b> Conditions such as osteoarthritis are more common in individuals with obesity due to the increased stress on weight-bearing joints and systemic inflammation. (Sources: Mayo Clinic, CDC)</li>
        <li><b>Severe COVID-19 Symptoms:</b> Individuals with obesity are at a higher risk for developing more severe complications if they contract COVID-19, including increased likelihood of hospitalisation, ICU admission, and mechanical ventilation. (Sources: CDC, NIDDK)</li>
        <li><b>Other Health Concerns:</b> Obesity also increases the risk for dyslipidemia, kidney disease, and complications related to pregnancy, fertility, and sexual function, in addition to mental health issues like depression and anxiety and challenges with physical functioning. (Sources: Mayo Clinic, CDC, NIDDK)</li>
        </ul>""", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: left; font-family: Times New Roman, serif; font-weight: bold; font-size: 25px'>Managing and Preventing Obesity</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: justify; font-size: 20px; font-family: Times New Roman; font-weight: normal'>Effective management and prevention of obesity are critical to reducing these health risks:</h2>", unsafe_allow_html=True)
    st.markdown("""<ul>
        <li><b>Dietary Changes:</b> Adopting a balanced diet with plenty of fruits, vegetables, whole grains, and lean proteins while practising portion control and reducing the intake of sugars and saturated fats is foundational. (Sources: WHO, Healthline)</li>
        <li><b>Physical Activity:</b> Engaging in at least 150 minutes of moderate aerobic activity or 75 minutes of vigorous activity weekly, along with muscle-strengthening exercises on two or more days a week, supports weight loss and overall health. (Sources: WHO, CDC)</li>
        <li><b>Behavioural Changes:</b> Healthy eating habits, regular physical activity, and effective stress management techniques are essential. Setting realistic weight loss goals can also motivate individuals toward sustained lifestyle changes. (Sources: NCBI, Healthline)</li>
        <li><b>Medical Interventions:</b> For some, medications and surgery may be considered when significant weight loss cannot be achieved through lifestyle changes alone. These options should be discussed with healthcare professionals. (Sources: WHO, NCBI)</li>
        <li><b>Seeking Professional Help:</b> Consulting healthcare professionals for personalised advice and treatment options is crucial for effective obesity management and prevention. (Sources: WHO, CDC)</li>
        </ul>""", unsafe_allow_html=True)

def page_facts_diabetes():
    st.markdown("<h1 style='text-align: center; color: #2A4258; font-family: American Typewriter, serif; font-weight: bold; font-size: 40px'>Facts about diabetes that you should be aware of</h1>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: left; font-family: Times New Roman, serif; font-weight: bold; font-size: 25px'>Understanding Type 2 Diabetes</h1>", unsafe_allow_html=True)
    st.markdown("""<h2 style='text-align: justify; font-size: 20px; font-family: Times New Roman; font-weight: normal'>
                <b>Definition:</b> Type 2 diabetes is a chronic health condition where the body struggles to metabolise glucose, a crucial energy source. This form of diabetes is characterised by the body's inability to use insulin effectively, though it still produces insulin, unlike Type 1 diabetes, where insulin production is minimal or non-existent. This impairment in insulin usage leads to elevated levels of glucose in the blood. (Sources: CDC, NIDDK, NCBI, WHO)
                <br><br>
                <b>Prevalence:</b> It is one of the most prevalent forms of diabetes, affecting millions worldwide, and its frequency is on the rise due to factors like aging populations and increasing rates of obesity and physical inactivity. Type 2 diabetes accounts for about 90% to 95% of all diagnosed cases of diabetes in adults. (Sources: CDC, NIDDK, NCBI, WHO)
                </h2>""", unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: left; font-family: Times New Roman, serif; font-weight: bold; font-size: 25px'>Causes and Risk Factors</h1>", unsafe_allow_html=True)
    st.markdown("""<ul>
        <li><b>Insulin Resistance:</b> A key feature of Type 2 diabetes is the body's inefficient use of insulin, leading to insulin resistance. This condition causes glucose to accumulate in the bloodstream instead of being absorbed by the cells, significantly raising blood sugar levels. (Sources: NIDDK, Mayo Clinic, Diabetes Australia)</li>
        <li><b>Obesity and Physical Inactivity:</b> These factors are strongly linked to the development of Type 2 diabetes, with obesity being a major contributor to insulin resistance. A sedentary lifestyle further exacerbates the risk, highlighting the importance of maintaining a healthy weight and engaging in regular physical activity. (Sources: NIDDK, Mayo Clinic, Diabetes Australia)</li>
        <li><b>Genetics and Family History:</b> The likelihood of developing Type 2 diabetes increases if there is a family history of the disease, indicating a genetic predisposition. Shared family behaviours and lifestyles further influence this risk. (Sources: NIDDK, Mayo Clinic, Diabetes Australia)</li>
        <li><b>Age, Race, and Ethnicity:</b> The risk of developing Type 2 diabetes increases with age. Additionally, certain racial and ethnic groups, including African Americans, Hispanic/Latino Americans, American Indians, and some Asian Americans and Pacific Islanders, are at a higher risk. (Sources: NIDDK, Mayo Clinic, Diabetes Australia)</li>
        <li><b>Other Health Issues:</b> Conditions such as high blood pressure, abnormal cholesterol levels, and a history of gestational diabetes are associated with an increased risk of developing Type 2 diabetes. These factors underscore the interconnectedness of various health conditions and the importance of comprehensive healthcare. (Sources: NIDDK, Mayo Clinic, Diabetes Australia)</li>
        </ul>""", unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: left; font-family: Times New Roman, serif; font-weight: bold; font-size: 25px'>Symptoms of Type 2 Diabetes</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: justify; font-size: 20px; font-family: Times New Roman; font-weight: normal'>Type 2 diabetes symptoms are often subtle and develop over time, making them easy to overlook. Key signs include:</h2>", unsafe_allow_html=True)
    st.markdown("""<ul>
        <li><b>Increased Thirst and Frequent Urination:</b> The need to expel excess glucose through urine leads to dehydration, causing increased thirst and a higher frequency of urination.</li>
        <li><b>Increased Hunger:</b> Even after eating, the body's inefficiency in using glucose can leave individuals feeling constantly hungry.</li>
        <li><b>Fatigue:</b> Energy levels drop as glucose remains in the bloodstream instead of fueling cells, resulting in tiredness.</li>
        <li><b>Blurred Vision:</b> Excess glucose can cause fluid to be drawn from the eyes, impairing vision.</li>
        <li><b>Slow-Healing Sores and Frequent Infections:</b> Elevated blood sugar levels can weaken the body's healing process and defence mechanisms.</li>
        <li><b>Numbness or Tingling:</b> High glucose levels may damage nerves, especially in the hands and feet, leading to numbness or tingling sensations.</li>
        <li><b>Unintended Weight Changes:</b> Unexpected weight loss or gain can be a consequence of disrupted glucose metabolism.</li>
        <li><b>Areas of Darkened Skin:</b> Patches of darkened skin, particularly in the armpits and neck, may signal insulin resistance. (Sources: Mayo Clinic, Diabetes Australia, NIDDK, CDC)</li>
        </ul>""", unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: left; font-family: Times New Roman, serif; font-weight: bold; font-size: 25px'>Managing Type 2 Diabetes</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: justify; font-size: 20px; font-family: Times New Roman; font-weight: normal'>Effective management of Type 2 diabetes focuses on maintaining blood sugar levels within a normal range:</h2>", unsafe_allow_html=True)
    st.markdown("""<ul>
        <li><b>Monitoring Blood Sugar:</b> Regularly checking blood sugar levels is crucial for adjusting diet, activity, and medications to manage diabetes effectively.</li>
        <li><b>Healthy Eating:</b> A diet rich in nutrients, low in fat and calories, and balanced in carbohydrates helps control blood sugar levels. Focusing on whole foods like fruits, vegetables, whole grains, and lean proteins is important.</li>
        <li><b>Physical Activity:</b> Regular physical activity helps lower blood sugar levels, boost insulin sensitivity, and maintain a healthy weight. Aim for at least 150 minutes of moderate to vigorous exercise per week.</li>
        <li><b>Medication and Insulin Therapy:</b> Many people with Type 2 diabetes require medication or insulin therapy to help manage their blood sugar levels. Adherence to prescribed treatments and close communication with healthcare providers are essential.</li>
        <li><b>Regular Checkups:</b> Ongoing medical care, including regular checkups, is important to monitor the condition and adjust treatment as necessary. This includes managing not only blood sugar but also cholesterol levels and blood pressure. (Sources: Mayo Clinic, Diabetes Australia, CDC, Better Health VIC)</li>
        </ul>""", unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: left; font-family: Times New Roman, serif; font-weight: bold; font-size: 25px'>Preventing Type 2 Diabetes</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: justify; font-size: 20px; font-family: Times New Roman; font-weight: normal'>Preventing Type 2 diabetes or delaying its onset is highly achievable through effective lifestyle modifications and proactive health measures:</h2>", unsafe_allow_html=True)
    st.markdown("""<ul>
        <li><b>Lifestyle Changes:</b> The cornerstone of Type 2 diabetes prevention lies in adopting and maintaining healthy lifestyle choices. Key strategies include:</li>
        <li><b>Maintaining a Healthy Weight:</b> Excess body fat, especially around the abdomen, increases the risk of developing Type 2 diabetes. Losing even a small amount of weight if you're overweight can significantly lower your risk.</li>
        <li><b>Engaging in Physical Activity:</b> Regular physical activity helps control weight, lowers blood sugar levels, and increases insulin sensitivity. Aim for at least 150 minutes of moderate aerobic activity or 75 minutes of vigorous activity each week, alongside muscle-strengthening exercises on two or more days.</li>
        <li><b>Eating a Well-Balanced Diet:</b> Focus on a diet rich in fruits, vegetables, whole grains, and lean proteins. Limit intake of refined sugars and saturated fats to help maintain optimal blood sugar levels and support a healthy weight. (Sources: NIDDK, CDC, Diabetes UK)</li>
        <li><b>Screening and Early Detection:</b> Regular screening for Type 2 diabetes is crucial, especially for those at higher risk due to factors like family history, age, overweight, and leading a sedentary lifestyle. Early detection through screening can facilitate timely interventions, such as lifestyle adjustments or medication, to prevent or delay the disease's progression. Screening recommendations can vary, but generally, adults over the age of 45 or those with risk factors should consider getting screened every 3 years. (Sources: NIDDK, CDC, Health.gov, Diabetes UK)</li>
        </ul>""", unsafe_allow_html=True)



def page_recommendations():
    st.title("Recommendations")
    st.write('Find recommendations based on the results')
    

    
def page_explore():
    st.title("Explore Obesity in the World/Australia")
    st.write('Explore data of obesity around the world and show how the person is in relation to the world/Australia')
    
def page_team():
    st.title("Know the team")
    st.write('Group 6 members')
    
def page_resources():
    st.title("Resources")
    st.write('Resources, papers, etc used. in the project')

def main():
    st.sidebar.title("Explore")
    
 

    # Create links for each page
    # Create buttons with icons for each page
    button_home = st.sidebar.button("🏠 Home")
    button_survey = st.sidebar.button("📝 Survey")
    button_results = st.sidebar.button("📊 Know Your Status")
    button_recommendation = st.sidebar.button("⭐ Recommendation") 
    button_explore = st.sidebar.button("🌐 Explore obesity in the World")
    button_team = st.sidebar.button("👥 Team")
    button_resources = st.sidebar.button("📚 Resources")


    
    # Initialize session state
    init_session_state()

    # Check which button is clicked and execute the corresponding function
    if button_home:
        st.session_state.selected_page = 'Home'

    if button_survey:
        st.session_state.selected_page = 'Survey'

    if button_results:
        st.session_state.selected_page = 'Know Your Status'

    if button_facts_diabetes:
        st.session_state.selected_page = 'Facts about Diabetes'

    if button_recommendation:
        st.session_state.selected_page = 'Recommendation'

    if button_explore:
        st.session_state.selected_page = 'Explore'

    if button_team:
        st.session_state.selected_page = 'Team'

    if button_resources:
        st.session_state.selected_page = 'Resources'

    # Execute the corresponding function based on the selected page
    if st.session_state.selected_page == 'Home':
        page_home()
    elif st.session_state.selected_page == 'Survey':
        page_survey()
    elif st.session_state.selected_page == 'Know Your Status':
        page_facts_obesity()
    elif st.session_state.selected_page == 'Facts about Diabetes':
        page_facts_diabetes()
    elif st.session_state.selected_page == 'Recommendation':
        page_recommendations()
    elif st.session_state.selected_page == 'Explore':
        page_explore()
    elif st.session_state.selected_page == 'Team':
        page_team()
    elif st.session_state.selected_page == 'Resources':
        page_resources()

if __name__ == "__main__":
    main()
    # Hehe

          
          




          
          