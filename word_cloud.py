#generate word could based on word input
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
%matplotlib inline
# lower max_font_size, change the maximum number of word and lighten the background:
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate("Microbiome, RND, Metagenomics, Data_Analysis, Transcriptomics, Gene_expression,  Python, R, Bioinformatics, Project_Managing, NGS, luminex, qPCR, Preclinical_models, IBD, CRC, GVHD, Machine_Learning, Correlation, Prediction")
#wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate("Stool, Saliva, Oral , Nasal , Skin , Tissue, Cultured_Microbe, Environmental")
#wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate("breast_cancer,colorectal_cancer, liver_cancer,pancreatic_cancer,skin_cancer,IBD/IBS,type_1_diabetes,type_2_diabetes,addiction, Alzheimer's_Disease, autoimmune_disorder,brain-gut_axis,cardiovascular_disease,environmental_microbiome,infectious_disease,maternal_infant_health,microbiome_standards,nutrition/diet,reproductive_health,waste_water_surveillance")
#wordcloud = WordCloud(max_font_size=50, max_words=100, width = 400, height = 600, background_color="white").generate("16S,ITS,WGS_Metagenomic,Complete_genome_sequencing,Virome,qPCR,Data_Analysis,Study_Consultation")

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

#font size based on the order of words
#installation of libraries needed.
