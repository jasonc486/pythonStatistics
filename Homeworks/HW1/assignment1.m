%% Shahreer Al Hossain | SS 340 ------------------
% Cause and Effect Assignment #1

Layoff_data = readtable("layoffs.csv");
Smoking_data = readtable("Wooldrridge smoking data.csv");

%-------------------------------------------------
%%
clc
clearvars -except Layoff_data Smoking_data
close all
%-------------------------------------------------
%% (2) Wooldrridge Smoking Data

Smoking_data_matrix = table2array(Smoking_data);

person_id = Smoking_data_matrix(:,1);

education = Smoking_data_matrix(:,2);

cig_price = Smoking_data_matrix(:,3);

white = Smoking_data_matrix(:,4);

age = Smoking_data_matrix(:,5);

income = Smoking_data_matrix(:,6);

num_of_cigs = Smoking_data_matrix(:,7);

restaurant_no_smoking = Smoking_data_matrix(:,8);

%-------------------------------------------------
% Summary Statistics of Education

num_of_obs_edu = numel(education);
mean_edu = mean(education);
median_edu = median(education);
std_edu = std(education);
min_edu = min(education);
max_edu = max(education);

person = 1:800;
figure;
scatter(person, education);

%-------------------------------------------------
% Summary Statistics of Cigarette Price

num_of_obs_cig_price = numel(cig_price);
mean_cig_price = mean(cig_price);
median_cig_price = median(cig_price);
std_cig_price = std(cig_price);
min_cig_price = min(cig_price);
max_cig_price = max(cig_price);

%-------------------------------------------------
% Summary Statistics of Age

num_of_obs_age = numel(age);
mean_age = mean(age);
median_age = median(age);
std_age = std(age);
min_age = min(age);
max_age = max(age);

%-------------------------------------------------
% Summary Statistics of Income

num_of_obs_income = numel(income);
mean_income = mean(income);
median_income = median(income);
std_income = std(income);
min_income = min(income);
max_income = max(income);

%-------------------------------------------------
% Summary Statistics of Number of Cigarettes Per Day

num_of_obs_cigs = numel(num_of_cigs);
mean_cigs = mean(num_of_cigs);
median_cigs = median(num_of_cigs);
std_cigs = std(num_of_cigs);
min_cigs = min(num_of_cigs);
max_cigs = max(num_of_cigs);

%-------------------------------------------------







