define build_docker_image
	docker image build --rm -t $(1):$(2) -f $(3) .
	docker tag $(1):$(2) $(1):latest
endef

DOCKER_IMAGE=pyapp
DOCKER_TAG=0.0.0

build_base_image: clean
	$(call build_docker_image,${DOCKER_IMAGE},${DOCKER_TAG},Dockerfile)

clean: clean_pyc

clean_pyc:
	find . -name "*.pyc" -exec rm -f {} \;
