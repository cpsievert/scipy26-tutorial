SLIDES_DIR := slides
EXERCISES_DIR := exercises
SITE_DIR := _site
QMD_FILES := $(sort $(wildcard $(SLIDES_DIR)/*.qmd))
HTML_FILES := $(QMD_FILES:.qmd=.html)

.PHONY: all slides clean preview serve help site

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

all: slides ## Build everything

slides: $(HTML_FILES) ## Render all slide decks

$(SLIDES_DIR)/%.html: $(SLIDES_DIR)/%.qmd $(SLIDES_DIR)/theme.scss
	cd $(SLIDES_DIR) && quarto render $(notdir $<)

preview: ## Open all rendered decks in the browser
	@for f in $(HTML_FILES); do open "$$f"; done

serve: ## Live-preview a deck (usage: make serve DECK=02-chatlas)
	@if [ -z "$(DECK)" ]; then \
		echo "Usage: make serve DECK=02-chatlas"; \
		exit 1; \
	fi
	cd $(SLIDES_DIR) && quarto preview $(DECK).qmd

site: slides ## Render website and stage slides under _site/slides
	quarto render
	mkdir -p $(SITE_DIR)/slides
	cp $(SLIDES_DIR)/*.html $(SITE_DIR)/slides/
	@if ls -d $(SLIDES_DIR)/*_files >/dev/null 2>&1; then cp -r $(SLIDES_DIR)/*_files $(SITE_DIR)/slides/; fi
	cp -r $(SLIDES_DIR)/images $(SITE_DIR)/slides/

clean: ## Remove rendered HTML and supporting files
	rm -f $(HTML_FILES)
	rm -rf $(SLIDES_DIR)/*_files
	rm -rf $(SITE_DIR)
