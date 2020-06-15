---
layout: post
title:  "Powerlifting Data Analysis"
date:   2020-06-11 11:22:55 +0100
categories: project upload
---

### Overview
#### Motivation

With the spare time I have available as a result of the Covid-19 induced lockdown, I have been self-studying Python, data analysis, and Machine Learning. I have developed a number of Machine Learning models, primarily with pre-cleaned data and with a defined goal in mind such as the competitions found on [Kaggle](https://www.kaggle.com/). While building these models was useful to understand some core ML concepts and become familiar with Python syntax, I wanted a project with which I could set my own goals and identify a variety of uses for the underlying data. I also wanted to be genuinely interested in the subject matter, and decided upon Powerlifting as a perfect basis for my first self-directed project. The sport is rapidly growing (the dataset upon which I based this project contains 250,000 individual competitive performances), is exceptionally easy to quantify numerically, and quickly became my primary hobby after leaving University.

#### Project Scope

For this project I wanted to make use of the [OpenPowerlifting](https://www.openpowerlifting.org/) dataset, for the purposes of Exploratory Data Analysis,
rudimentary visualisations, and facilitate comparison between an individual's competitive performance and the wider Powerlifting community. Functionality that I have currently implemented includes:

 - **Visualisation:** Plotting trajectories of Total (a metric for absolute strength), Wilks score (a metric for relative strength) and Bodyweight over the course of individuals' competitive careers
 - **Lift Analysis:** Allowing an individual to identify where their individual lifts stand relative to the wider community, both in terms of percentile and variation from the respective means
 - **Competition Classification:** Basic use of a Machine Learning Clustering model to classify competitions into Regional, National, and International meets
 - **Performance Prediction:** Allowing a user to determine their likely placing at an upcoming competition based on historical data, or retroactively assess the standard of competition at a past meets

Functionality that I wish to implement in the future includes:

 - Allow input of user data through an on-site UI
 - Refine the implemented Machine Learning model to produce better predictions
 - Identify how reliance on certain lifts varies through weight classes
 - Illustrate inverse correlations between lifts due to biomechanical advantages and disadvantages
 - Demonstrate and model the rapid growth of the sport
 - Do competitors tend to favour different lifts throughout their careers?

 Each heading contains a hyperlink to the underlying Python code, viewable on Github.

### [Data Cleaning](https://github.com/SamPurle/PowerProject/blob/master/Cleaning.py)

The OpenPowerlifting dataset is community-maintained, with a variety of different managers that are responsible for uploading competition data from many different federations as they occur across 65 different countries. It appears the site utilises a relational database at the back-end, as individual competitors are able to link a variety of different Social Media accounts to their competitive profiles, which in turn are tied to Meets in which they have competed. This infrastructure is not available to site visitors however, and the raw data is available as a simple '.csv' file.

The presence of many different federations within the raw data has the consequence that competitors do not have a Unique ID tied to them, and can only be identified by name. As such, detection of individual competitors is entirely dependent on the name they elected to use while entering any given competition. As an example of this I appear as two distinct competitors within the dataset: as Samuel Purle on 2019-04-06, and then as Sam Purle on 2020-01-26. This will introduce a degree of noise into the raw data, the removal of which I do not believe to be possible without the use of extensive and complex string operations. Even subsequent to this, the issue would not be entirely alleviated due to the presence of competitors from many different countries and cultures within the data - where naming conventions differ substantially from those in the West.

### [Growth of the sport](https://github.com/SamPurle/PowerProject/blob/master/GrowthModelling.py)

Powerlifting as a sport has experienced rapid growth over recent years. There are likely a multitude of reasons for this. One of which has been the growing popularity of "Raw" lifting as opposed to the original "Equipped" lifting, which has resulted in the sport becoming more accessible to the gym-going population. Additionally, health and fitness has become a prominent subject on a variety of social media platforms (most notably Instagram and YouTube), which has resulted in greater awareness of the sport.

{:refdef: style="text-align: center;"}
<img src="{{site.url}}/{{site.baseurl}}/assets/SportGrowth.png">
{: refdef}

It will be intesting to see the impact which the Covid-19 pandemic has upon the influx of new competitors to thee sport.

### [General Trends](https://github.com/SamPurle/Powerlifting/blob/master/Plotting.py)

After data cleaning and calculating the Elapsed Time since competitors' first Meets, it is possible to plot the general trajectories followed by individuals over the course of their competitive careers. It would be interesting to identify an inflexion point where the positive impact of Training Age begins to be surpassed by the negative impact of biological aging, although unfortunately there is insufficient information relating to biological age within the dataset. Only data on Age Class is present, which is not specific enough to be useful for this purpose (the 24-39 year old "Senior" class is far too wide to be able to identify any meaningful trend).

The three metrics I wish to investigate are:

- Total - a metric for Absolute Strength
- Wilks - a metric for Relative Strength
- Bodyweight

#### Total

A lifter's Total is generally their primary competitive goal - to lift the highest combined total between their Squat, Bench Press and Deadlift.

{:refdef: style="text-align: center;"}
<img src="{{site.url}}/{{site.baseurl}}/assets/TotalPlot.png">
{: refdef}


- Both sexes see a significant increase in Total over the first couple of years of competing. This plateaus in Men after ~2 years of competing, but continues to increase marginally in Women until ~6 years into competing. Both sexes see a significant drop in absolute strength after 8 years or more of competing, presumably as the effects of biological aging outpace the improvements made with increased training age.



#### Wilks

The Wilks score was developed as a method of comparing the relative strengths of lifters across multiple weight classes and genders. It is effectively a "power to weight ratio" used to score performance within competitive Powerlifting. Although lean muscle mass is an enormous component in determining a lifter's ability to generate force, other factors also influence this:

 - Muscle fibre diameter
 - Actin : Myosin ratio within muscle fibres
 - Motor Neuron Recruitment, which is heavily influenced by adrenaline
 - Angle of interplay between tendons and attached bones (with can vary significantly as muscles grow throughout an athlete's career)

{:refdef: style="text-align: center;"}
<img src="{{site.url}}/{{site.baseurl}}/assets/WilksPlot.png">
{: refdef}


- On average Men have an initial Wilks score roughly 15% higher than Women.

- Over the course of their competitive careers, on average Women see a 33% increase in Wilks score (peaking at around 380 ~8 years into competing), relative to 18% in Men (peaking at 390 ~3 years into competing).

The fact the Women have a lower initial Wilks could be due to unfairly calculated coefficients, but looking at other plots it makes more sense that Women start competing earlier on in their lifting careers than Men.

#### Bodyweight

It is relatively commonplace for lifters to undertake the decision to move towards higher weight classes as they progress in their lifting careers. This is in part a by-product of the natural propensity to gain muscle through resistance training, but also due to phenomenon that lifters will generally become more competitive as they gain body mass. An analysis of the biomechanics involved shows that - all other things being equal - taller lifters have to generate more force with a smaller mass of muscle to lift an equivalent weight as a shorter, stockier competitor.

{:refdef: style="text-align: center;"}
<img src="{{site.url}}/{{site.baseurl}}/assets/BodyweightPlot.png">
{: refdef}


- Male lifters tend to put on 5-10kg of weight in their first 2-4 years of competing. Average body-weight in Men continues to increase after their Total plateaus, which explains Men's Wilks scores peaking much earlier than Women's.

- Bodyweight of Female lifters doesn't change significantly over the course of their competitive careers, aside from a slight decrease towards the end. Although a social scientist would be better equipped to explain this, this could either be due to Women being more disciplined on average in terms of maintaining a low body fat percentage, or being less willing to put on weight to chase after a perceived competitive advantage.

### [Lift Analysis](https://github.com/SamPurle/PowerProject/blob/master/LiftAnalysis.py)
#### Comparison with the wider community

The relative strengths of a individual's lifts have substantial implications on way they will approach a competitive situation, as well as providing insight on areas on which to focus training and potentially review technique. Biomechanics and a lifter's bodily proportions play a significant role in determining which lifts an individual will naturally favour, and it is somewhat rare for an individual to be equally strong in all three lifts relative to the general Powerlifting population.

Although similar tools currently exist online, these are of limited use for individuals interested in lifting competitively. A novice/intermediate Powerlifter will often be classified as having advanced/elite level strength by such tools.

{:refdef: style="text-align: center;"}
<img src="{{site.url}}/{{site.baseurl}}/assets/LiftPlot.png">
{: refdef}

This overview can be further broken down by showing the distributions of each individual lift:

{:refdef: style="text-align: center;"}
<img src="{{site.url}}/{{site.baseurl}}/assets/SquatDist.png">
{: refdef}

{:refdef: style="text-align: center;"}
<img src="{{site.url}}/{{site.baseurl}}/assets/BenchDist.png">
{: refdef}

{:refdef: style="text-align: center;"}
<img src="{{site.url}}/{{site.baseurl}}/assets/DeadliftDist.png">
{: refdef}

{:refdef: style="text-align: center;"}
<img src="{{site.url}}/{{site.baseurl}}/assets/TotalDist.png">
{: refdef}


#### Takeaways

The above plots help quantify what I already suspected: my Squat is by far my biggest competitive advantage, which I would benefit from leveraging by placing other competitors on the back foot after the first event within a competition.

Despite substantial effort on my part, my Bench Press continues to be a competitive weak-point. I believe this is primarily due to past injury and naturally long arms relative to my height - which causes a loaded barbell to create a greater turning moment at my shoulder. I also plan to investigate the hypothesis that lighter lifters (such as myself) are much more lower-body dependent the heavier lifters. My natural leaning towards lower-body strength limits the amount of muscle I can carry around my torso while staying in the lighter weight classes. As such, I expect to see an improvement in the competitiveness of my Bench Press as I move up in Weight Class and the effect of this limitation is mitigated.

My Deadlift is marginally stronger than other competitive lifters in my weight class. I believe the lower body strength that provides the foundation for my Squat to be the primary reason for this. Moving forwards, I plan to capitalise on this strength by continuing to develop my "Sumo" Deadlift technique - which differs substantially from my current "Conventional" technique and relies on many of the same muscle groups as the Squat.

### [Clustering](https://github.com/SamPurle/PowerProject/blob/master/ClusteringModel.py)
#### A Machine Learning model to classify Competitions

There is a high level of variation in the calibre of lifters seen at Competitions, between federations, countries, and even between weight classes - such as the infamously "stacked" 83kg IPF class where a large number of Men fall due to the natural size of their frames.

In order to predict placing at an upcoming competition, it would be useful to be able to approximate the level of difficulty that is expected. Clearly a National level Meet with strict Qualifying Totals will see a higher standard of competitions than a Regional University Meet, where the majority of lifters are only just beginning their lifting careers and are likely to fall in the Junior and Sub-Junior age classes.

{:refdef: style="text-align: center;"}
<img src="{{site.url}}/{{site.baseurl}}/assets/ClusterPlot.png">
{: refdef}

Currently this model is a proof-of-concept, and is not functional in a particularly meaningful way. I am relatively unfamiliar with using unlabelled data, and as such this is my first attempt at a clustering model. I considered approaching this problem by developing a Random Forest Classifier and providing a small list of labelled Competitions that could be extrapolated to the dataset as whole. However, my current plan is to think more carefully about parameter selection to be able to develop a clustering model with more distinct separation between competitions.


### [Performance Predictor](https://github.com/SamPurle/Powerlifting/blob/master/PerformancePredictor.py)
#### A tool to predict competitive performance

Even for lifters that enter competitions with their own self-determined goals other than placing, it is useful to be able to approximate where they are likely to fall within the Meet's rankings. Information on where a lifter's total falls within the general population's distribution can be combined with a description of the level of the meet and labels from the clustering algorithm above. This can be used to calculate the percentile on which a competitor falls among historical competitive performances from lifters in their weight class competing at their level. A probability distribution can then be generated based on the number of confirmed competitors attending an upcoming meet.

To generate this distribution it was necessary to make use of the mathematical "choose" function in order to correctly calculate probability. There is only one way in which a competitor can place 1st - by beating every other competitor in their class. However, there are many different way in which a competitor could place 2nd - any one of the other competitors in their class could place higher than them.

{:refdef: style="text-align: center;"}
<img src="{{site.url}}/{{site.baseurl}}/assets/PlacingPlot.png">
{: refdef}

The plot above shows my predicted placing amongst a competition consisting of twelve 74kg lifters at a Regional level, based on my pre-lockdown lifts. I plan to introduce functionality to allow input from site visitors.

### [Lift dependency](https://github.com/SamPurle/PowerProject/blob/master/LiftDependency.py)
#### Weight Class

{:refdef: style="text-align: center;"}
<img src="{{site.url}}/{{site.baseurl}}/assets/M_Dependency.png">
{: refdef}

{:refdef: style="text-align: center;"}
<img src="{{site.url}}/{{site.baseurl}}/assets/F_Dependency.png">
{: refdef}

### Final thoughts
