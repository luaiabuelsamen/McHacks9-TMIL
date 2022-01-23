from searchtweets import ResultStream, gen_rule_payload, load_credentials, collect_results

premium_search_args = load_credentials("~/.twitter_keys.yaml",
                                       yaml_key="search_tweets_premium",
                                       env_overwrite=False)
# testing with a sandbox account
rule = gen_rule_payload("beyonce", results_per_call=100)

print(rule)  # debug purposes

tweets = collect_results(rule,
                         max_results=100,
                         result_stream_args=premium_search_args)  # change this if you need to

tweetsfinal = [tweet.all_text for tweet in tweets]
