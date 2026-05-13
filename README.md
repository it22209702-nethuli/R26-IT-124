# R26-IT-124
# Edge AI–Enabled Post-Harvest Quality Management for Pineapple Warehousing and Transport

# Project Overview

This project focuses on developing an AI-assisted post-harvest monitoring and freshness assessment system for pineapples in Sri Lankan warehouse and transportation environments. The main objective of the system is to reduce post-harvest losses by improving the way pineapples are monitored, graded, and tracked after harvesting. The proposed solution combines Edge AI, image processing, IoT-based environmental monitoring, grading mechanisms, and GPS traceability into a single integrated platform.

The system is mainly designed for warehouse operators, transport coordinators, and quality assurance personnel who are involved in handling pineapples during storage and transportation. By introducing automated freshness assessment and monitoring features, the system aims to reduce manual errors and improve decision-making during post-harvest operations.

# System Components
# Component 01 – IoT Environmental Monitoring

This component focuses on monitoring the environmental conditions inside warehouses and transportation vehicles. Sensors are used to collect data such as temperature, humidity, and gas levels that can affect pineapple quality during storage and transport.

The collected sensor data will later be integrated with the other components of the system to support freshness analysis and warehouse monitoring activities.

Main Technologies
- Raspberry Pi
- DHT22 Sensor
- MQ Gas Sensor
- GPS Module
- MQTT Communication

Main Features
- Real-time environmental monitoring
- Temperature and humidity tracking
- Gas detection support
- GPS-based transport monitoring
- Offline-capable monitoring support

# Component 02 – Edge AI Freshness Assessment Using Image Processing

This component focuses on identifying the freshness level of pineapples using image processing and Edge AI technologies. Images captured using Raspberry Pi camera modules are processed and classified into different freshness categories.

The prototype currently uses a CNN-based transfer learning model trained using Edge Impulse Studio. The model was trained using pineapple image datasets collected for different freshness levels.

Freshness Categories
- Fresh
- Early Deterioration
- Moderate Deterioration
- Spoiled

AI Model Information
The image classification model was developed using:
- Convolutional Neural Network (CNN)
- MobileNetV2-based transfer learning
- Edge Impulse Studio

The trained model was exported as an '.eim' deployment file for future Raspberry Pi integration.

Current Progress
The following tasks have already been completed:
- Dataset preparation
- Image classification workflow setup
- Initial model training
- Confusion matrix generation
- Backend API prototype development
- Local backend testing using Flask and Postman

Main Features
- Image-based freshness classification
- Edge AI processing
- Offline inference capability
- REST API integration support
- Real-time prediction response generation

Challenges Identified
One of the main challenges identified during implementation was distinguishing between nearby freshness stages such as early deterioration and moderate deterioration due to gradual visual differences between pineapple images.

This highlighted the importance of integrating additional sensor data such as gas sensing in future development stages to improve overall classification accuracy.

# Component 03 – Pineapple Grading and Pricing System

This component focuses on grading pineapples according to size and ripeness after the freshness assessment stage is completed. Separate AI models are planned for size classification and ripeness identification using pineapple exterior images.

Size Categories
- Small
- Medium
- Large

Ripeness Categories
- Green
- Half Yellow
- Full Yellow

Main Outputs
- Size category
- Ripeness category
- Quality grade

Main Features
- Automated grading process
- AI-based size classification
- Ripeness identification
- Quality-based recommendations

Design Contribution
This component helps reduce inconsistencies in manual grading and supports warehouse operators in making better storage and dispatch decisions based on pineapple quality.


# Component 04 – GPS and QR Code–Based Traceability System

This component focuses on introducing a pricing mechanism where pineapple prices can be determined based on freshness level, ripeness stage, and size category. Then it will be tracking pineapple batches throughout the warehouse and transportation process. QR codes are generated for each batch and scanned at different checkpoints to maintain traceability records.

GPS integration is also used to monitor transportation routes and maintain location history for pineapple shipments.

Main Features
- QR code generation
- Batch tracking
- GPS-based route monitoring
- Warehouse checkpoint logging
- Supply chain traceability

Main Outputs
- Batch movement history
- Transportation records
- Freshness-linked tracking information
- Environmental condition history

Design Contribution
This component improves transparency within the pineapple supply chain and helps identify issues related to spoilage, transportation delays, or environmental risks during storage and transport activities.

#Backend API Prototype

A backend API prototype was developed using Flask to support the freshness assessment workflow. The backend currently supports image uploads and returns freshness prediction responses in JSON format.

The prototype was tested locally using Postman and VS Code.

Technologies Used
- Python
- Flask
- OpenCV
- REST APIs

Current Backend Features
- Local backend deployment
- Image upload handling
- JSON response generation
- API endpoint testing
- Integration-ready architecture


# Model Deployment Information
The trained freshness classification model was exported from Edge Impulse as an .eim deployment file. This file contains the trained CNN model and deployment configuration required for future edge-device integration.

-Model Information
-Model Type: CNN
-Architecture: MobileNetV2
-Platform: Edge Impulse Studio
-Deployment File Type: .eim


# UI/UX Design Plan

Initially, the project architecture was evaluated for both web-based and mobile-based implementations. After discussing the operational requirements of warehouse monitoring and transport management activities, the team decided to continue the system development mainly as a mobile application while maintaining backend API support for future scalability.

The mobile application approach was selected because it provides easier accessibility for warehouse staff, transport coordinators, and quality assurance officers who may need to monitor pineapple batches and freshness information directly through smartphones or handheld devices during transport and warehouse operations.

The planned mobile application will communicate with the backend system through REST APIs and provide real-time access to freshness information, grading results, environmental monitoring data, and traceability records.

# Planned Mobile Application Features
- Real-time freshness monitoring
- Environmental condition tracking
- Pineapple grading information
- GPS-based transport monitoring
- QR code scanning support
- Batch history viewing
- Alert and notification support
- Warehouse dashboard summaries

# Mobile Application Advantages
- Easier portability during warehouse inspections
- Faster access to freshness information
- Convenient monitoring during transportation
- Better accessibility for field-level users
- Real-time notifications and alerts

# Chosen Color Palette

The planned mobile application interface follows a tropical-industrial color palette inspired by pineapple agriculture while maintaining a clean and professional appearance suitable for logistics and warehouse environments.

- Primary Yellow - Pineapple Gold - #F4B400
- Secondary Green - Leaf Green - #2E7D32 
- Background - Soft Cream - #FFF8E1 
- Accent Orange - Harvest Orange - #FB8C00 
- Neutral Dark - Charcoal - #263238 
- White - Clean White - #FFFFFF 

# Freshness Status Colors
- Fresh → Green
- Early → Yellow
- Moderate → Orange
- Spoiled → Red

# Planned UI Design Style

The mobile application is planned using a clean and modern design style that supports easy readability and smooth user interaction in warehouse and transportation environments.

# Planned Design Characteristics
- Minimal and user-friendly layouts
- Simple navigation structure
- Easy-to-read dashboards
- Card-based monitoring screens
- Large status indicators for freshness levels
- Quick access to QR scanning and tracking functions

The interface is also planned to support users with limited technical experience by maintaining simple workflows and clear visual indicators throughout the application. 

# Current Challenges and Future Improvements

Although the current prototype demonstrates the overall workflow of the proposed solution, several improvements are planned for future development stages:

-Raspberry Pi deployment
-TensorFlow Lite integration
-Improved dataset collection
-Real-time edge inference
-Olfactory sensor integration
-GPS dashboard visualization
-Mobile application support
-Cloud synchronization

# Future Expansion Possibilities

Although the current focus is on mobile application development, the backend architecture is designed using REST APIs, which allows future integration with:
- Web dashboards
- Cloud monitoring systems
- Warehouse management systems
- Export monitoring platforms

This provides flexibility for future expansion without requiring major architectural modifications.

