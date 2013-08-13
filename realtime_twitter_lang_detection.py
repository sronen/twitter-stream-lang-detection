from collections import Counter
import cld, tweetstream

if __name__ == "__main__":
	langs = Counter()
	while True:
		try:
			with tweetstream.FilterStream("jcodameta", "T3stcct!", track=["MediaLabIO"]) as stream:
				for	 tweet in stream:
					tweet_text = tweet.get("text")
					try:
						lang = cld.detect(tweet_text.encode('utf-8'))[0]
						langs[lang] += 1
						print langs, tweet_text
					except:
						print "error1"
						continue
		except:
			print "error2"
			continue