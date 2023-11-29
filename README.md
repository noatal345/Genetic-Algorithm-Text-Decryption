# Genetic Algorithm Text Decryption

## Overview

This project implements a genetic algorithm to decrypt a text file encoded with a substitution cipher. The algorithm is written in Python and is composed of several files that serve different purposes. Here's a brief overview of each file:

- **py.config**: Configuration file specifying parameters such as population size, elite group size, mutation rate, number of generations, number of runs, and the set of valid characters for decoding.

- **py.general**: Helper file that creates dictionaries from external files (txt.Freq2Letter, txt.LetterFreq, txt.dict) to optimize the running process.

- **py.class_Fitness**: A class responsible for calculating the fitness score of each individual in the generation based on word frequency and letter permutations.

- **py.functions_generation**: Contains functions for creating the initial generation, performing crossover between parents, correcting missing letters, and introducing mutations.

- **py.main**: The main program that runs the genetic algorithm 10 times and selects the best individual (permutation) with the highest fitness score for decoding.

## Components of the Genetic Algorithm

### Representation of Solutions

At the start of each algorithm run, a population of permutations of the ABC letters is generated. Each generation is represented as a list of dictionaries, where each dictionary corresponds to a permutation.

### Evaluation Function

The fitness score of each individual is calculated based on the frequency of single letters, pairs of letters, and the percentage of words appearing in the dictionary. The total fitness is a combination of these factors.

### Performing the Crossover Operation

A new generation is created by selecting parents based on their fitness scores using a probability calculation. 25% of the best individuals (elite) are passed to the next generation without crossover, while the remaining 75% undergo crossover to create new individuals.

### Realization of Mutations

Mutations are introduced in the new generation with a predefined probability. Only non-elite individuals have a chance to undergo mutations, where letters are randomly selected for mutation.

### Early Convergence Problem

Several approaches are explored to address the early convergence problem, including increasing mutation rates, checking for repeated best-fit individuals, and saving results over multiple runs.

## Usage

To run the decryption algorithm, execute the `py.main` file. Adjust the parameters in the `py.config` file as needed.

## Results

The algorithm runs until convergence or a specified number of generations. The best permutation after multiple runs is chosen for decoding the cipher.



