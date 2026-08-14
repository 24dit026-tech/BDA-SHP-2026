
# Practical 4: Find the Maximum Temperature Recorded for Each Year of NCDC Data using MapReduce

**Name:** Prisha Kalola  
**Student ID:** 24DIT026  
**Course:** CSUE301 - Big Data Analytics

---

## Aim

To find the maximum temperature recorded for each year from NCDC weather data using the MapReduce approach.

---

## Problem Definition

A meteorological research organization maintains historical weather records collected from various weather stations. The objective is to process the NCDC weather dataset and identify the maximum temperature recorded for each year using MapReduce.

---

## Tasks Performed

1. Created and examined the NCDC weather dataset.
2. Developed a Python Mapper program to extract the year and temperature values from each record.
3. Generated intermediate key-value pairs in the form `(year, temperature)`.
4. Developed a Python Reducer program to determine the maximum temperature for each year.
5. Executed the MapReduce process and verified the generated output.
6. Analyzed the yearly maximum temperatures and identified the hottest year.
7. Calculated the minimum temperature for each year as a supplementary task.
8. Calculated the average yearly temperature as a supplementary analysis.

---

## Dataset

The practical uses a sample NCDC-style weather dataset containing historical temperature records.

Each record contains:

```text
Year,Temperature
