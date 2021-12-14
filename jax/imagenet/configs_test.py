"""Tests for imagenet.configs."""

from absl.testing import absltest
from absl.testing import parameterized

from google3.third_party.google_research.google_research.aqt.jax.imagenet.configs import resnet101_bfloat16
from google3.third_party.google_research.google_research.aqt.jax.imagenet.configs import resnet50_w4
from google3.third_party.google_research.google_research.aqt.jax.imagenet.configs import resnet50_w4_a2_fixed
from google3.third_party.google_research.google_research.aqt.jax.imagenet.configs import resnet50_w8
from google3.third_party.google_research.google_research.aqt.jax.imagenet.configs import resnet50_w8_a8_fixed
from google3.third_party.google_research.google_research.aqt.jax.imagenet.configs.paper import resnet50_bfloat16
from google3.third_party.google_research.google_research.aqt.jax.imagenet.configs.paper import resnet50_w4_a4_auto


class ConfigsTest(parameterized.TestCase):

  @parameterized.parameters(
      dict(config_dict_module=resnet50_bfloat16),
      dict(config_dict_module=resnet101_bfloat16))
  def test_unquantized_config(self, config_dict_module):
    config = config_dict_module.get_config()
    self.assertIsNone(config.prec)

  @parameterized.parameters(
      dict(config_dict_module=resnet50_w8, prec=8),
      dict(config_dict_module=resnet50_w4, prec=4))
  def test_weights_only_quantized_config(self, config_dict_module, prec):
    config = config_dict_module.get_config()
    self.assertEqual(config.weight_prec, prec)
    self.assertIsNone(config.quant_act.bounds)

  @parameterized.parameters(
      dict(config_dict_module=resnet50_w4_a4_auto, weight_prec=4, act_prec=4),
      dict(config_dict_module=resnet50_w4_a2_fixed, weight_prec=4, act_prec=2),
      dict(config_dict_module=resnet50_w8_a8_fixed, weight_prec=8, act_prec=8))
  def test_fully_quantized_quantized_config(self, config_dict_module,
                                            weight_prec, act_prec):
    config = config_dict_module.get_config()
    self.assertEqual(config.weight_prec, weight_prec)
    self.assertEqual(config.quant_act.prec, act_prec)


if __name__ == '__main__':
  absltest.main()
