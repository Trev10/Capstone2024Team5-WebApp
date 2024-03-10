import sqlite3
import os

def read_image_as_blob(image_path):
    with open(image_path, 'rb') as file:
        return file.read()

# Connect to the SQLite database
conn = sqlite3.connect('products.db')
cursor = conn.cursor()

# Construct the relative path to the images directory
images_base_path = os.path.join('images')

# List of tuples representing products to insert
# Each tuple contains: (product_type, model_name, description)
products_to_insert = [
    ('GCM', 'Dexcom G6 Mobile CGM System', 'The Dexcom G6 Mobile CGM System offers real-time glucose monitoring every five minutes for both type 1 and type 2 diabetes patients, accessible on smart devices anytime and anywhere. It eliminates the need for fingersticks for diabetes treatment decisions, providing glucose data directly to your smartphone. The system, which is easy to use and lasts up to 10 days per application, has been shown to lower A1C levels and improve time spent in the target glucose range.', os.path.join(images_base_path, 'dexcom-g6.png')),
    ('GCM', 'Dexcom G7 Mobile CGM System', 'The Dexcom G7 Mobile CGM System revolutionizes diabetes management by delivering real-time glucose data directly to your smartphone or smartwatch without the need for fingersticks, allowing for smarter decisions about food and activity. With an outstanding accuracy rating of 8.2 persent overall MARD for adults and 8.1% MARD for children, it provides reliable information to confidently manage diabetes in the moment. The systems alerts, including personalized options, ensure timely responses to glucose fluctuations, offering greater peace of mind, while its small and discreet sensor design enhances comfort and wearability.', os.path.join(images_base_path, 'dexcom-g7.jpg')),
    ('GCM', 'FreeStyle Libre', 'The FreeStyle Libre System simplifies glucose monitoring with a 1-second scan that captures data from the sensor, storing up to 90 days worth of glucose information without requiring fingerstick calibration. Its accurate sensor readings, verified through the FreeStyle Libre User Manual, are easily accessible via a backlit color touchscreen, allowing users to view their current glucose reading, trend arrow, and an 8-hour glucose history graph with just a quick scan.', os.path.join(images_base_path, 'freestyle.png')),
    ('GCM', 'FreeStyle Libre 3 System', 'The FreeStyle Libre 3 Sensor represents a significant advancement in glucose monitoring, boasting a discreet design worn on the upper arm, providing continuous glucose measurement day and night. With updates every minute, it sends data directly to a compatible smartphone, offering up to 14 days of wear and water resistance for uninterrupted use during daily activities. Its acclaimed for its accuracy, aiding in reducing hypoglycemia and enhancing overall glucose control, while its easy application, thin profile, and environmentally friendly design make it a convenient and sustainable choice for users.', os.path.join(images_base_path, 'freestyle3.jpg')),
    ('GCM', 'FreeStyle Libre2', 'The FreeStyle Libre 2 is a continuous glucose monitoring system that helps people with diabetes manage their blood sugar levels. It consists of a sensor worn on the arm that measures glucose levels and a reader or smartphone app that displays the data. The sensor can be worn for up to 14 days and eliminates the need for finger pricks.', os.path.join(images_base_path, 'freestyle2.png')),

    ('Insulin Pump', 'Omnipod 5 Tubeless, automated insulin delivery', 'The Omnipod 5 Tubeless automated insulin delivery system combines the benefits of glucose control from an Automated Insulin Delivery System with the freedom of a tubeless device, offering the best of both worlds in one solution. Clinical studies have demonstrated significant improvements in time spent within the target glucose range, particularly in children and adolescents, with up to 3.7 hours per day increase. The system consists of three simple parts the Pod, Dexcom G6 CGM, and the Omnipod 5 App working seamlessly together to automatically adjust insulin delivery every 5 minutes based on real-time CGM data, providing continuous glucose management without the need for constant manual adjustments.', os.path.join(images_base_path, 'omnipod5.png')),
    ('Insulin Pump', 'Tandem T-slim Basal IQ Insulin pump', 'The Tandem t-slim Basal IQ Insulin Pump integrates Basal-IQ predictive low-glucose suspend technology, which helps users spend less time worrying about lows by predicting and preventing them through responsive insulin delivery, turning insulin delivery on and off as frequently as every five minutes. Operating silently in the background, it offers a reduction in sensor time below 70 mg/dL and instills confidence in users with its ease of use. Basal-IQ technology utilizes CGM values to anticipate glucose levels, suspending insulin delivery if levels are predicted to drop below 80 mg/dL, with no fingerstick calibrations required when integrated with the Dexcom G6 CGM system. The pump allows bolusing from a smartphone via the t:connect mobile app and offers remote software updates, ensuring users benefit from the latest technology throughout the pumps warranty period.', os.path.join(images_base_path, 'tandem-basal.jpg')),
    ('Insulin Pump', 'Tandem T-slim Control IQ Insulin Pump', 'The Tandem t-slim Control IQ Insulin Pump employs advanced Control-IQ technology, a hybrid closed-loop system that predicts and helps prevent highs and lows by automatically adjusting insulin levels based on Dexcom G6 continuous glucose monitoring (CGM) readings. It also offers automatic correction boluses to prevent hyperglycemia and includes optional settings for Sleep and Exercise Activities, providing more control over treatment ranges. Designed to increase time spent within the target range, the system utilizes Dexcom G6 CGM values to predict glucose levels and adjust insulin delivery accordingly, all without the need for fingerstick calibrations. With visual icons on the pump screen indicating insulin delivery status, users can easily monitor and manage their glucose levels with confidence.', os.path.join(images_base_path, 'tandem-control.png')),
    ('Insulin Pump', 'The Omnipod System', 'The Omnipod System offers an innovative approach to continuous insulin delivery, providing the benefits of insulin pump therapy with enhanced flexibility and freedom due to its tubeless design. With customizable insulin delivery settings, it mimics the insulin release of a healthy pancreas through basal rates and bolus doses, offering control tailored to individual needs. The system consists of a tubeless, waterproof insulin pump called a Pod, controlled by a wireless Personal Diabetes Manager (PDM), providing up to 72 hours of insulin delivery without wires or tubes. Simple to use, users fill the Pod, apply it to their body, and start insulin delivery with the touch of a button, making diabetes management less stressful and more convenient.', os.path.join(images_base_path, 'omnipod.png')),

    ('Blood Glucose Test Strip', 'Accu-Chek Aviva Plus Blood Glucose Test Strips', 'The Accu-Chek Aviva Plus Blood Glucose Test Strips offer accurate and clear readings, making them essential for daily blood glucose monitoring. These strips are designed for self-testing purposes only, filling quickly with a tiny drop of blood and undergoing over 150 system integrity checks to ensure reliability. Compatible with the Accu-Chek Aviva meter, they deliver fast results in just 5 seconds and can be used for testing on the finger, palm, or forearm. Manufactured in the USA with both domestic and imported materials, these test strips provide advanced accuracy for precise glucose measurement, promoting effective diabetes management.', os.path.join(images_base_path, 'accu-check-aviva-plus.jpg')),
    ('Blood Glucose Test Strip', 'Accu-Chek SmartView Test Strips for Nano', 'The Accu-Chek SmartView Test Strips, available in a 50-count pack, ensure accurate results with each use, specifically designed for compatibility with the Accu-Chek Nano unit. These strips eliminate the need for coding and feature a SmartPack vial, making it easy to retrieve a single strip without spillage. Offering convenience, they allow for blood application anywhere on the strip, not limited to a small area, ensuring reliable results consistently. Simple to use and suitable for logging readings to a smartphone, these test strips provide users with a hassle-free experience in blood glucose monitoring.', os.path.join(images_base_path, 'accu-chek-smartview.jpg')),
    ('Blood Glucose Test Strip', 'Accu-Chek SmartView Blood Glucose Test Strips', 'The Accu-Chek SmartView Blood Glucose Test Strips offer advanced accuracy, instilling confidence in blood sugar results. Designed for ease of use, these strips are suitable for individuals of all ages and fill quickly with a tiny 0.6-microliter drop at any point along the tip. Each box contains 50 test strips, providing users with convenience and reliability in blood glucose monitoring.', os.path.join(images_base_path, 'accu-check-SmartView-TestStrips.jpg')),
    ('Blood Glucose Test Strip', 'Ascensia Contour Blood Glucose Test Strips', 'The Ascensia Contour Blood Glucose Test Strips feature Sip-in Sampling® Technology, ensuring each strip draws in the correct amount of blood for accurate testing. The inclusion of a window facilitates easy observation of blood filling in the strip. Additionally, the flip-top bottle design allows for convenient opening, closing, and handling of the strips, enhancing user experience during glucose monitoring.', os.path.join(images_base_path, 'ascensia-contour.jpg')),
    ('Blood Glucose Test Strip', 'CONTOUR NEXT TEST STRIPS', 'The Contour Next Test Strips, compatible with all Bayers Contour Next meters, offer convenience and accuracy in blood glucose monitoring. They come in 50, 100, 200, or 400 count packages and feature no-coding technology for simplified use. With a small blood sample size of 0.6 ul and a fast 5-second countdown, these strips provide efficient testing with personalized settings and adjustable alarms. Their innovative strip technology ensures accurate results right out of the box, enhancing user confidence in daily testing and management of blood glucose levels.', os.path.join(images_base_path, 'contour-blood-meter.jpg')),
    ('Blood Glucose Test Strip', 'Contour Blood Glucose Test Strips', 'The Contour Blood Glucose Test Strips are designed for use with Bayers Contour® Blood Glucose meter, providing reliable results for glucose monitoring. Each box contains 50 test strips, offering users an ample supply for regular testing and management of blood glucose levels.', os.path.join(images_base_path, 'contour-blood.jpg')),
    ('Blood Glucose Test Strip', 'EasyMax GDH Test Strips', 'The EasyMax GDH Test Strips, developed by Oak Tree International Holdings, Inc. / EPS Bio Technology Corp., have received FDA approval for individual and multiple patient use. These GDH-FAD strips and meters are designed for quantitative measurement of glucose in venous and fresh capillary whole blood, providing more accurate readings (+15%) according to FDA guidelines and detecting under-fill in the strips. It is the only FDA-approved system in the market for multiple patient use. Intended for at-home use by a single patient with diabetes, the system aids in monitoring the effectiveness of diabetes control and should not be shared. Not suitable for neonates or diagnosing diabetes, it employs GDH-FAD enzyme test strips, requiring a small blood sample of 0.6 ul and providing fast results in just 5 seconds. The large strips facilitate better handling during testing.', os.path.join(images_base_path, 'easymax-blood-meter.png')),
    ('Blood Glucose Test Strip', 'FreeStyle Blood Glucose Test Strips', 'The FreeStyle Blood Glucose Test Strips are designed for use with both the FreeStyle and Flash Blood Glucose Monitoring Systems. Each box contains 50 test strips, providing users with an ample supply for blood glucose testing.', os.path.join(images_base_path, 'freestyle-blood.jpg')),
    ('Blood Glucose Test Strip', 'FREESTYLE PRECISION NEO BLOOD GLUCOSE TEST STRIPS', 'The FreeStyle Precision Neo Blood Glucose Test Strips offer ease of use and accuracy, compatible with the FreeStyle Precision Neo meter and the FreeStyle Libre 14 day Flash Glucose Monitoring systems. These over-the-counter test strips require no coding and feature a small sample size of 0.6 microliters, making testing convenient and efficient. Individually wrapped for on-the-go use, they allow for top fill or end fill blood application and can be re-applied within 5 seconds. The foil-wrapped test strips are protected from air and moisture, ensuring reliability. Each box contains 50 test strips, providing users with an ample supply for glucose testing. Its important to note the indications and important safety information for the FreeStyle Libre 14 day system, including contraindications, warnings, and limitations, which should be carefully reviewed before use.', os.path.join(images_base_path, 'Freestyle-Neo-Test-Strips.jpg')),
    ('Blood Glucose Test Strip', 'OneTouch Verio Test Strips', 'The OneTouch Verio Test Strips are designed for blood sugar testing, requiring only 0.4 uL of blood for accurate results. Featuring a visual confirmation window, users can easily determine when enough blood has been applied. These test strips do not require manual coding, simplifying the testing process. With a side-fill design, they can be used on either side, providing flexibility and convenience. Additionally, the test strips offer quick wicking action, ensuring fast and reliable results.', os.path.join(images_base_path, 'onetouche-verio.jpg')),
    ('Blood Glucose Test Strip', 'OneTouch Ultra 2 Blood Glucose Test Strips', 'The OneTouch Ultra 2 Blood Glucose Test Strips are designed for blood sugar testing, featuring DoubleSure® Technology that automatically checks each blood sample twice for enhanced accuracy. With FastDraw™ capillary action, these strips draw the blood sample in less than 1 second, ensuring swift and efficient testing. Additionally, they provide visual confirmation of an adequate blood sample, simplifying the testing process. Backed by eight years of proven accuracy, users can trust these test strips for reliable glucose monitoring.', os.path.join(images_base_path, 'onetouch-ultra-blood.jpg')),
    ('Blood Glucose Test Strip', 'OneTouch Ultra Blue Blood Glucose Test Strip', 'The OneTouch Ultra Blue Blood Glucose Test Strips are designed for blood sugar testing, incorporating DoubleSure® technology to automatically check each blood sample twice for enhanced accuracy. With FastDraw® capillary action, these strips efficiently draw the blood sample in less than 1 second, ensuring swift and convenient testing. Additionally, they provide visual confirmation of an adequate blood sample, facilitating ease of use during glucose monitoring.', os.path.join(images_base_path, 'onetouch-ultra.jpg')),
    ('Blood Glucose Test Strip', 'Prodigy No Coding Blood Glucose Test Strips', 'The Prodigy No Coding Blood Glucose Test Strips are designed for quick and accurate blood glucose testing, compatible with the Prodigy AutoCode, Pocket, and Voice meters. They feature no coding requirement for ease of use and work with all Prodigy meters. Approved for alternate site testing (AST), these strips employ capillary action to draw the blood sample into the test strip automatically, ensuring convenience and efficiency. Unlike strips using GDH-PQQ technology, Prodigy AutoCode strips utilize glucose oxidase technology, providing safer and more accurate results. Each pack contains 50 strips, and this listing includes 2 packs, providing users with an ample supply for glucose monitoring needs.', os.path.join(images_base_path, 'Prodigy-Test-Strips.jpg')),
    ('Blood Glucose Test Strip', 'Ketostix® Urine Reagent Strip', 'Ketostix® Urine Reagent Strip is utilized to test urine for ketones, commonly used by diabetics to monitor increased metabolism and to maintain a healthy diet regimen.', os.path.join(images_base_path, 'ketostix.jpg')),

    ('Glucose Meter', 'Contour Blood Glucose Meter', 'The Contour Blood Glucose Meter is equipped with several innovative features for efficient and reliable glucose monitoring. The SmartLight feature provides an instant indicator of blood glucose results, offering users immediate feedback. Second-Chance sampling prompts users to reapply blood if the initial sample was insufficient, ensuring accurate readings. Additionally, the SmartAlerts function alerts users when their blood glucose level is at a critical high or low, helping them manage their condition more effectively.', os.path.join(images_base_path, 'contour-blood-meter.jpg')),
    ('Glucose Meter', 'Accu-Chek Guide Me meter', 'The Accu-Chek Guide Me meter offers spill-resistant SmartPack® vial for convenience, allowing users to take one strip without spills. Its flexible blood application permits a small drop of blood anywhere along the strip, while results are automatically logged to the mySugr app for smartphone accessibility. With Accu-Chek Guide test strips providing advanced 10/10 accuracy, coupled with a large, easy-to-read display, users can trust reliable results and effortless readability.', os.path.join(images_base_path, 'accu-chek-guideme.jpg')),
    ('Glucose Meter', 'EasyMax NG Blood Glucose Meter', 'The EasyMax NG Blood Glucose Meter features a no-coding system for simplified use, along with a strip ejector for convenience. Its back-lit display enhances visibility in various lighting conditions, while a robust rubber protector ensures durability. With high reliability for over 20,000 continuous tests, users can trust consistent and accurate results with this meter.', os.path.join(images_base_path, 'easymax-blood-meter.png')),
    ('Glucose Meter', 'OneTouch Verio Flex Blood Glucose Meter', 'The OneTouch Verio Flex Blood Glucose Meter utilizes ColorSure™ technology, providing instant feedback on blood sugar levels status. Its compact and slim design ensures portability for on-the-go monitoring. Seamlessly syncing data with the free OneTouch Reveal® mobile app, it offers convenient tracking and management. Additionally, it utilizes OneTouch Verio® test strips, known for their five years of proven accuracy across a wide range of blood sugar levels.', os.path.join(images_base_path, 'one_touch_verio_flex.jpg')),
    ('Glucose Meter', 'OneTouch Verio Flex meter', 'The OneTouch Verio Flex meter simplifies glucose monitoring with easy one-step meal tagging for convenience. Featuring a color display and illuminated test strip port, it facilitates testing in low-light conditions. Equipped with ColorSure™ technology, on-screen messages promptly notify users of repeated highs and lows for efficient management. Utilizing OneTouch Verio® test strips, it ensures five years of proven accuracy across a wide range of blood glucose levels.', os.path.join(images_base_path, 'onetouch-meter.jpg')),
    ('Glucose Meter', 'OneTouch Verio IQ meter', 'The OneTouch Verio IQ meter assists users in comprehending how insulin, meal intake, and lifestyle impact blood sugar levels. Equipped with ColorSure™ technology, it provides on-screen notifications of repeated highs and lows for effective monitoring. Featuring easy one-step meal tagging and a color display with an illuminated test strip port, it ensures convenient testing even in low-light conditions.', os.path.join(images_base_path, 'onetouch-verio-iq-meter.jpg')),
    ('Glucose Meter', 'OneTouch Verio meter', 'The OneTouch Verio meter offers convenient blood glucose monitoring with ColorSure™ technology, providing instant feedback on blood sugar levels status. It automatically delivers messages with each result, offering feedback on the users current status without the need to scroll or push buttons.', os.path.join(images_base_path, 'One-Touch-Verio.jpg')),
    ('Glucose Meter', 'OneTouch UltraMini Meter', 'The OneTouch UltraMini Meter is a compact blood glucose monitor designed to fit easily in a purse or pocket for convenient portability.', os.path.join(images_base_path, 'onetouch-ultra-blood.jpg')),
    
]

# SQL command with parameters
sql = '''INSERT INTO product (product_type, model_name, description, image) VALUES (?, ?, ?, ?)'''

# Execute the command for each product
for product in products_to_insert:
    # Unpack tuple to separate image path from other data
    product_type, model_name, description, image_relative_path = product
    # Assuming your script's working directory is the project root, construct the full path
    image_full_path = os.path.join(os.getcwd(), image_relative_path)
    # Read image file as binary data
    image_blob = read_image_as_blob(image_full_path)
    # Insert product data along with image blob
    cursor.execute(sql, (product_type, model_name, description, image_blob))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Products inserted successfully.")