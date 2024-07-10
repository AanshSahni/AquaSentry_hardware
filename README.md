Aqua Sentry: IoT-Based Automated Swimming Pool Maintenance System

Welcome to the Aqua Sentry project! This repository contains the code and documentation for "Aqua Sentry," an advanced IoT-based system designed to automate the maintenance of swimming pool water quality.

Table of Contents:
  Introduction
  Features
  Components Required
  System Architecture
  Installation
  Usage
  
Methodology:
  Formulas and Calculations
  Results and Discussion

Introduction:
Maintaining optimal water quality in swimming pools is essential for ensuring the health and safety of swimmers. Traditional methods for monitoring and managing water quality, such as manual testing and chemical adjustments, can be labor-intensive, time-consuming, and prone to human error. Aqua Sentry leverages IoT technology to provide a more efficient and automated approach to pool maintenance.

Features:
  1. Continuous monitoring of pH, chlorine levels, and total alkalinity
  2. Automated chemical dosing to maintain optimal water quality
  3. Real-time data processing using edge and fog computing
  4. LoRa technology for efficient data transmission
  5. Cost-effective and easy to deploy

Components Required:
  1. Power Supply (12V)
  2. Relay Modules (for each dispenser
  3. Microcontroller (ESP32/Arduino Nano)
  4. pH Sensor
  5. ORP Sensor
  6. Water Pumps
  7. LoRa Transmitter/Receiver
  8. Centralized Computer/Raspberry Pi
  
System Architecture:

The Aqua Sentry system is designed using a layered architecture consisting of edge, fog, and cloud layers. Each layer has distinct responsibilities to ensure efficient data collection, analysis, and control for maintaining optimal water quality in swimming pools.
  1. Edge Layer:
    •	Sensors and Microcontrollers: The edge layer comprises various sensors and microcontrollers deployed at strategic points within the pool. The primary sensors used include pH sensors, and ORP (Oxidation-Reduction Potential) sensors.
    •	Sensor Placement: To ensure comprehensive monitoring, sensors are placed at multiple locations in the pool. This helps in capturing accurate and localized data.
    •	Data Collection: Sensors continuously collect data on water parameters, which is then transmitted to the fog layer using LoRa (Long Range) communication technology. This choice of communication ensures low power consumption and long-range data transmission capabilities.
  2. Fog Layer:
    •	Data Aggregation and Processing: The fog layer consists of a centralized computer system that aggregates data from the edge devices.
    •	Real-Time Analysis: The system processes the incoming data in real-time to determine if the water parameters deviate from their ideal ranges.
    •	Control Mechanisms: Based on the analysis, the fog layer sends instructions back to the edge devices to dispense appropriate chemicals (such as pH increasers or decreasers, and chlorine) to maintain water quality.
    •	Algorithms Used: The fog layer employs specific algorithms to estimate chlorine levels from ORP readings and calculate total alkalinity based on pH and temperature data.
  3. Cloud Layer:
    •	Data Storage: All processed data is sent to the cloud for long-term storage and historical analysis.
    •	User Interface: The cloud layer provides a user-friendly interface for pool maintenance personnel and users to monitor the water quality in real-time. It offers alerts and insights based on the collected data.

Formulas and Calculations:
  pH Adjustment
    Increasing pH with Sodium Carbonate:
      Dosage (g) = Volume (L) × 0.16 × (Target pH - Current pH)
      Factors:
        Volume: Volume of the pool in liters.
        Target pH: Desired pH level.
        Current pH: Current pH level of the pool.
  Chlorine Adjustment
      Increasing Chlorine Levels:
        Dosage (mg) = Volume (L) × 2 × (Target ORP - Current ORP)
      Factors:
      Volume: Volume of the pool in liters.
      Target ORP: Desired ORP level.
      Current ORP: Current ORP level of the pool.

Results and Discussion:
The Aqua Sentry system has demonstrated significant improvements in maintaining pool water quality. The automated adjustments reduce manual intervention and ensure consistent water conditions, enhancing the safety and experience for swimmers.
The current model of Aqua Sentry supports only the use of a pH sensor. Future iterations will include support for ORP and other sensors to provide a more comprehensive water quality management solution.
