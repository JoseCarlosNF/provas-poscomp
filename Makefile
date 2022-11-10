VERSION='0.1.0'

build-dev:
	docker build -t josecarlosnf/provas-poscomp:dev-${VERSION} --target dev .

dev:
	docker run --rm --name provas_poscomp -p 80:8000 -v $(PWD)/provas_poscomp:/app josecarlosnf/provas-poscomp:dev-${VERSION}
