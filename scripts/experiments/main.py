import logging
import hydra
from omegaconf import DictConfig, OmegaConf



log = logging.getLogger(__name__)

@hydra.main(version_base=None, config_path="conf", config_name="config")
def main(cfg: DictConfig) -> None:
	"""Hydra entrypoint that wires the configuration into the run function."""

	logging.basicConfig(level=logging.INFO)
	log.info("Configuration:\n%s", OmegaConf.to_yaml(cfg))

	# TODO: Replace with your actual experiment code.
	log.info("Running experiment placeholder...")


if __name__ == "__main__":
	main()
