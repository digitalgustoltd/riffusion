"""
Data model for the riffusion API.
"""

from dataclasses import dataclass


@dataclass
class PromptInput:
    """
    Parameters for one end of interpolation.
    """

    # Text prompt fed into a CLIP model
    prompt: str

    # Random seed for denoising
    seed: int

    # Denoising strength
    denoising: float = 0.75

    # Classifier-free guidance strength
    guidance: float = 7.0


@dataclass
class InferenceInput:
    """
    Parameters for a single run of the riffusion model, interpolating between
    a start and end set of PromptInputs. This is the API required for a request
    to the model server.
    """

    # Start point of interpolation
    start: PromptInput

    # End point of interpolation
    end: PromptInput

    # Interpolation alpha [0, 1]. A value of 0 uses start fully, a value of 1
    # uses end fully.
    alpha: float

    # Number of inner loops of the diffusion model
    num_inference_steps: int = 50

    # Which seed image to use
    # TODO(hayk): Convert this to a string ID and add a seed image + mask API.
    seed_image_id: int = 0


@dataclass
class InferenceOutput:
    """
    Response from the model server. Contains a base64 encoded spectrogram image and a base64
    encoded MP3 audio clip.
    """

    image: str
    audio: str