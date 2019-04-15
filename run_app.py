# input_channel = SlackInput('xoxp-609656943046-594287361475-609338617687-764a996e985d0651d4e688f7fdd7bccc',
# 							'xoxb-609656943046-599490439985-37Q7nhNcH2plLlkrSSWKGDom',
# 							'nkWJYcOOd01qnGssI7FwJ100',
# 							'True'
# 							)





from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig

nlu_interpreter = RasaNLUInterpreter('./models/current/nlu')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/current/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)

input_channel = SlackInput('******' #your bot user authentication token
                           )
agent.handle_channels([input_channel], 5004, serve_forever=True)

