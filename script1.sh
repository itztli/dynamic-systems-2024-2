#!/bin/bash

for initialCondition in {1..100..1};
do
  ./example2.py $initialCondition > output/data_$initialCondition.dat
done


