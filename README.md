## McHacks9 Team — Risko

# Inspiration
As new concepts such as Decentralized Finance, Web 3.0, and Layer 2 Blockchains evolve, more and more investors are looking into new types of investment vehicles to secure their profit. Cryptocurrencies are by nature highly volatile and speculative assets. However, cryptocurrencies are by nature highly volatile and speculative assets, and therefore present a high barrier of entry. This led us to our idea of creating something that examines the positivity and confidence of the market. With a machine learning model that can analyze sentiment in real time, everyone can get a brief idea of how others think and use that to help make decisions.

# What it does
Risko is a web app that lets users choose a cryptocurrency (coin) and provides insights to how others are feeling about the prospect of coins of interest. Utilizing Twitter API, Risko features real-time data analysis and returns the corresponding “optimism” score based on recent tweets other investors shared. 

After receiving a request from the user, Risko gathers relevant tweets from Twitter. Each related tweet is then passed into a pre-trained NLP (transformer-based) sentiment prediction model, and the returned probability is used to calculate the “positivity” of this one tweet. The final “optimism” score of a coin is then calculated as the average of the “positivity” of all related tweets. 

# How we built it
Jupyter Notebook, Python, and Flask used for backend. HTML, CSS used for frontend. Validation of modular functions was done by random test cases.

# Challenges we ran into
Twitter API requests, data cleaning and preprocessing, frontend/backend integration, selecting appropriate ML model, visual design and layout of web app.

# Accomplishments that we're proud of
Made use of API to obtain and analyze data in real time, deployed transformers to analyze text sentiment, developed reactive web app with dynamic visuals.

# What we learned
How to request/clean up data from websites with an API, how to make use of pre-trained ML models, how to organize file dependencies. Limitations of free APIs and pre-trained ML models.

# What's next for Risko
Fine tuning of transformer model for market confidence/fear (vix) index in crypto space.
Filtering of spam accounts/tweets, weigh options based on retweets.
Training based on feedback from professional analysts.

