# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.

import gettext

from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler,
    AbstractRequestInterceptor,
    AbstractExceptionHandler,
)
import ask_sdk_core.utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

import serial

arduino = None


def send(text):
    arduino.write(bytes(text, "utf-8"))


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global arduino
        arduino = serial.Serial(
            port="/dev/tty.SLAB_USBtoUART", baudrate=9600, timeout=0.1
        )
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _("¡Bienvenido!")

        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class TurnOnFanIntentHandler(AbstractRequestHandler):
    """Handler for turning the fan on Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TurnOnFanIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _("Ventilador encendido")
        send("a")

        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class TurnOffFanIntentHandler(AbstractRequestHandler):
    """Handler for turning the fan off Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TurnOffFanIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _("Ventilador apagado")
        send("b")

        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class TurnOnWhiteLedIntentHandler(AbstractRequestHandler):
    """Handler for turning the white led on Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TurnOnWhiteLedIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _("Luz blanca encendida")
        send("c")

        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class TurnOffWhiteLedIntentHandler(AbstractRequestHandler):
    """Handler for turning the white led off Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TurnOffWhiteLedIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _("Luz blanca apagada")
        send("d")

        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class TurnOnYellowLedIntentHandler(AbstractRequestHandler):
    """Handler for turning the white led on Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TurnOnYellowLedIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _("Luz amarilla encendida")
        send("e")

        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class TurnOffYellowLedIntentHandler(AbstractRequestHandler):
    """Handler for turning the white led off Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TurnOffYellowLedIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _("Luz amarilla apagada")
        send("f")

        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class TurnOnLedsIntentHandler(AbstractRequestHandler):
    """Handler for turning the white led off Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TurnOnLedsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _("Luces encendidas")
        send("g")

        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class TurnOffLedsIntentHandler(AbstractRequestHandler):
    """Handler for turning the white led off Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TurnOffLedsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _("Luces apagadas")
        send("h")

        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class OpenDoorIntentHandler(AbstractRequestHandler):
    """Handler for turning the white led off Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("OpenDoorIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _("Puerta abierta")
        send("i")

        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class CloseDoorIntentHandler(AbstractRequestHandler):
    """Handler for turning the white led off Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CloseDoorIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _("Puerta cerrada")
        send("j")

        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class OpenWindowIntentHandler(AbstractRequestHandler):
    """Handler for turning the white led off Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("OpenWindowIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _("Ventana abierta")
        send("k")

        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class CloseWindowIntentHandler(AbstractRequestHandler):
    """Handler for turning the white led off Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CloseWindowIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _("Ventana cerrada")
        send("l")

        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class EnableAutoLedsIntentHandler(AbstractRequestHandler):
    """Handler for enabling the auto leds Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("EnableAutoLedsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _("Luces automáticas activadas")
        send("m")

        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class DisableAutoLedsIntentHandler(AbstractRequestHandler):
    """Handler for disabling the auto leds Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("DisableAutoLedsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _("Luces automáticas desactivadas")
        send("n")

        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _("data.HELP_MSG")

        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.CancelIntent")(
            handler_input
        ) or ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _("Adios")

        return handler_input.response_builder.speak(speak_output).response


class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech = "No estoy segura de poder ayudarte con eso."
        # reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(speech).response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.
        arduino.close()

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        _ = handler_input.attributes_manager.request_attributes["_"]
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = _("data.REFLECTOR_MSG").format(intent_name)

        return (
            handler_input.response_builder.speak(speak_output)
            # .ask("add a reprompt if you want to keep the session open for the user to respond")
            .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """

    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _("error")

        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class LocalizationInterceptor(AbstractRequestInterceptor):
    """
    Add function to request attributes, that can load locale specific data
    """

    def process(self, handler_input):
        locale = handler_input.request_envelope.request.locale
        i18n = gettext.translation(
            "data", localedir="locales", languages=[locale], fallback=True
        )
        handler_input.attributes_manager.request_attributes["_"] = i18n.gettext
