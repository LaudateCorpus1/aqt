"""Resnet50 quantized model."""

from google3.third_party.google_research.google_research.aqt.jax.imagenet.configs import base_config


def get_config(quant_target=base_config.QuantTarget.weights_and_fixed_acts):
  """Gets Resnet50 config for 4b weights and 2b fixed activation quantization.

  conv_init and last dense layer not quantized as these are the most
  sensitive layers in the model.

  Args:
   quant_target: quantization target, of type QuantTarget.

  Returns:
   ConfigDict instance.
  """
  config = base_config.get_config(
      imagenet_type=base_config.ImagenetType.resnet50,
      quant_target=quant_target)
  config.weight_prec = 4
  config.quant_act.prec = 2
  config.model_hparams.conv_init.weight_prec = None
  config.model_hparams.conv_init.quant_act = None
  config.model_hparams.dense_layer.weight_prec = None
  config.model_hparams.dense_layer.quant_act = None
  return config
