# Practical 3: Implement Word Count / Frequency Program using MapReduce

**Name:** Prisha Kalola  
**Student ID:** 24DIT026  

## Aim

To implement a Word Count / Frequency program using Hadoop MapReduce and analyze word frequencies from news article data stored in HDFS.

## Problem Definition

A digital publishing company stores thousands of news articles and blog posts in HDFS. The objective is to process the text data using MapReduce and generate word frequency statistics to identify frequently occurring words and analyze trending topics.

## Tasks Performed

1. Configured the Hadoop environment using Docker.
2. Created and uploaded news article datasets to HDFS.
3. Implemented the Mapper to generate `(word, 1)` intermediate key-value pairs.
4. Implemented the Reducer to aggregate word occurrences.
5. Executed the MapReduce job and stored the output in HDFS.
6. Identified the Top 10 most frequently occurring words.
7. Excluded common stop words from the analysis.
8. Compared word frequencies using multiple input files.
9. Evaluated execution time using datasets of different sizes.

## Technologies Used

- Hadoop 3.4.3
- HDFS
- MapReduce
- Java 11
- Docker
- GitHub Codespaces

## Mapper and Reducer

### Mapper

The Mapper reads each input line, converts words to lowercase, removes punctuation, ignores predefined stop words, and generates intermediate pairs:

`(word, 1)`

### Reducer

The Reducer receives each word with its associated values and calculates the total frequency:

`(word, total_frequency)`

## Top 10 Words — Single Input File

| Rank | Word | Frequency |
|---:|---|---:|
| 1 | data | 6 |
| 2 | technology | 5 |
| 3 | artificial | 4 |
| 4 | intelligence | 4 |
| 5 | companies | 3 |
| 6 | better | 2 |
| 7 | business | 2 |
| 8 | businesses | 2 |
| 9 | cloud | 2 |
| 10 | computing | 2 |

## Multiple Input File Analysis

The MapReduce program was executed using both `news.txt` and `news2.txt` as input files. The combined processing generated updated word frequencies, demonstrating that MapReduce can process multiple input files together.

## Performance Analysis

| Dataset | Size | Processing Time |
|---|---:|---:|
| Small | 809 bytes | 5.303 s |
| Medium | 8,090 bytes | 4.559 s |
| Large | 80,900 bytes | 5.550 s |

The execution time does not increase linearly for these small datasets because MapReduce has fixed framework, JVM, Map, Shuffle, and Reduce overhead. For substantially larger datasets, distributed processing becomes more beneficial.

## Key Questions / Analysis

### Q1. What is the role of Mapper and Reducer in the Word Count application?

The Mapper processes input text and generates intermediate `(word, 1)` pairs. The Reducer receives each word with its values and sums them to produce the final word frequency.

### Q2. How are intermediate key-value pairs generated and processed?

The Mapper tokenizes each input line and generates a key-value pair `(word, 1)` for every valid word. Hadoop then performs shuffle and sort operations to group identical words before passing them to the Reducer.

### Q3. How does HDFS store and distribute the input dataset?

HDFS stores files as blocks and distributes those blocks across DataNodes. The NameNode maintains metadata about the files and blocks, while DataNodes store the actual data.

### Q4. What advantages does MapReduce offer for processing large datasets?

MapReduce provides distributed and parallel processing, fault tolerance, scalability, and the ability to process large datasets across multiple machines.

### Q5. How does the execution time vary with dataset size?

For the tested small datasets, execution time remained relatively similar because fixed MapReduce startup and processing overhead dominated the execution. The measured times were 5.303 s, 4.559 s, and 5.550 s for small, medium, and large datasets respectively.

## Supplementary Problems

### 1. Top 10 frequently occurring words

The Top 10 words were identified after excluding common stop words.

### 2. Exclusion of stop words

Words such as `a`, `an`, `the`, `is`, `and`, and `to` were excluded by the Mapper before frequency counting.

### 3. Comparison of multiple input files

The MapReduce job was executed using both `news.txt` and `news2.txt`. The results demonstrated that frequencies are combined when multiple input files are processed through the same HDFS input directory.

## Result

The Hadoop MapReduce Word Count application was successfully implemented and executed. The Mapper generated intermediate `(word, 1)` pairs, while the Reducer aggregated them to produce final word frequencies. The Top 10 frequently occurring words were identified, stop words were excluded, multiple input files were processed, and execution times were compared for datasets of different sizes.

## Conclusion

The practical demonstrated the use of HDFS and MapReduce for distributed text processing. The experiment showed how the Mapper, Shuffle and Sort phase, and Reducer work together to calculate word frequencies. The performance experiment also demonstrated that MapReduce has fixed execution overhead, which is more noticeable for small datasets, while its distributed processing model is suitable for large-scale data processing.

