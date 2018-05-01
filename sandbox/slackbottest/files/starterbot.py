import os
import time
import re
from slackclient import SlackClient
from textblob import TextBlob

# instantiate Slack client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"
POS_DICT = {"CC": "Coordinating conjunction",
	"CD": "Cardinal number",
	"DT": "Determiner",
	"EX": "Existential there",
	"FW": "Foreign word",
	"IN": "Preposition or subordinating conjunction",
	"JJ": "Adjective",
	"JJR": "Adjective, comparative",
	"JJS": "Adjective, superlative",
	"LS": "List item marker",
	"MD": "Modal",
	"NN": "Noun, singular or mass",
	"NNS": "Noun, plural",
	"NNP": "Proper noun, singular",
	"NNPS": "Proper noun, plural",
	"PDT": "Predeterminer",
	"POS": "Possessive ending",
	"PRP": "Personal pronoun",
	"PRP$": "Possessive pronoun",
	"RB": "Adverb",
	"RBR": "Adverb, comparative",
	"RBS": "Adverb, superlative",
	"RP": "Particle",
	"SYM": "Symbol",
	"TO": "to",
	"UH": "Interjection",
	"VB": "Verb, base form",
	"VBD": "Verb, past tense",
	"VBG": "Verb, gerund or present participle",
	"VBN": "Verb, past participle",
	"VBP": "Verb, non-3rd person singular present",
	"VBZ": "Verb, 3rd person singular present",
	"WDT": "Wh-determiner",
	"WP": "Wh-pronoun",
	"WP$": "Possessive wh-pronoun",
	"WRB": "Wh-adverb"}

def parse_bot_commands(slack_events):
	"""
		Parses a list of events coming from the Slack RTM API to find bot commands.
		If a bot command is found, this function returns a tuple of command and channel.
		If its not found, then this function returns None, None.
	"""
	for event in slack_events:
		if event["type"] == "message" and not "subtype" in event:
			user_id, message = parse_direct_mention(event["text"])
			if user_id == starterbot_id:
				return message, event["channel"]
	return None, None

def parse_direct_mention(message_text):
	"""
		Finds a direct mention (a mention that is at the beginning) in message text
		and returns the user ID which was mentioned. If there is no direct mention, returns None
	"""
	matches = re.search(MENTION_REGEX, message_text)
	# the first group contains the username, the second group contains the remaining message
	return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def handle_command(command, channel):
	"""
		Executes bot command if the command is known
	"""

	print('received command: ', command)
	# Default response is help text for the user
	default_response = "Not sure what you mean. Try *{}*.".format(EXAMPLE_COMMAND)

	# Finds and executes the given command, filling in response
	response = None
	# This is where you start to implement more commands!
	command_textblob = TextBlob(command)
	command_tags = command_textblob.tags
	command_POS = [g+': '+POS_DICT[h] for (g,h) in command_tags]
	response = '    ---------    '.join(command_POS)

	respond_with_message(response, channel)

def respond_with_message(response, channel, default_response='Hmm, something isnt right here.'):
	# Sends the response back to the channel
	slack_client.api_call(
		"chat.postMessage",
		channel=channel,
		text=response or default_response
	)

def get_nouns_verbs(tagged_sentence):
	nv = [g for (g,h) in command_tags if g in ['NN','NNS','NNP','NNPS','VB','VBD','VBG','VBN','VBP','VBZ'] ]
	


if __name__ == "__main__":
	if slack_client.rtm_connect(with_team_state=False):
		print("Starter Bot connected and running!")
		# Read bot's user ID by calling Web API method `auth.test`
		starterbot_id = slack_client.api_call("auth.test")["user_id"]
		while True:
			command, channel = parse_bot_commands(slack_client.rtm_read())
			if command:
				handle_command(command, channel)
			time.sleep(RTM_READ_DELAY)
	else:
		print("Connection failed. Exception traceback printed above.")
