from flask import Flask
from flask_ask_sdk.skill_adapter import SkillAdapter
from ask_sdk_core.skill_builder import SkillBuilder
from intents import *



# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


SKILL_ID = "amzn1.ask.skill.aa9cdd99-6644-4a98-b3de-459905570fc1"
app = Flask(__name__)
skill_builder = SkillBuilder()
skill_adapter = None


@app.route("/alexa", methods=["POST"])
def invoke_skill():
    
    return skill_adapter.dispatch_request()


def main():
    global skill_adapter

    skill_builder.add_request_handler(LaunchRequestHandler())
    skill_builder.add_request_handler(TurnOnFanIntentHandler())
    skill_builder.add_request_handler(TurnOffFanIntentHandler())
    skill_builder.add_request_handler(TurnOnWhiteLedIntentHandler())
    skill_builder.add_request_handler(TurnOffWhiteLedIntentHandler())
    skill_builder.add_request_handler(TurnOnYellowLedIntentHandler())
    skill_builder.add_request_handler(TurnOffYellowLedIntentHandler())
    skill_builder.add_request_handler(TurnOnLedsIntentHandler())
    skill_builder.add_request_handler(TurnOffLedsIntentHandler())
    skill_builder.add_request_handler(OpenDoorIntentHandler())
    skill_builder.add_request_handler(CloseDoorIntentHandler())
    skill_builder.add_request_handler(OpenWindowIntentHandler())
    skill_builder.add_request_handler(CloseWindowIntentHandler())
    skill_builder.add_request_handler(EnableAutoLedsIntentHandler())
    skill_builder.add_request_handler(DisableAutoLedsIntentHandler())
    skill_builder.add_request_handler(HelpIntentHandler())
    skill_builder.add_request_handler(CancelOrStopIntentHandler())
    skill_builder.add_request_handler(FallbackIntentHandler())
    skill_builder.add_request_handler(SessionEndedRequestHandler())
    # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers
    skill_builder.add_request_handler(IntentReflectorHandler())
    skill_builder.add_global_request_interceptor(LocalizationInterceptor())
    skill_builder.add_exception_handler(CatchAllExceptionHandler())

    skill_adapter = SkillAdapter(
        skill=skill_builder.create(), skill_id=SKILL_ID, app=app
    )

    app.run(port=5000)


if __name__ == "__main__":
    main()

