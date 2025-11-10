# null

export function openSearch() {
  document.getElementById("search-bar-entry").click();
}


<div className="relative w-full pt-12 pb-0">
  <div id="background-div" className="absolute inset-0" />

  <div className="text-black dark:text-white relative z-10 flex flex-col md:flex-row gap-6" style={{ maxWidth: '70rem', marginLeft: 'auto', marginRight: 'auto', paddingLeft: '1.25rem', paddingRight: '1.25rem' }}>
    <div className="flex-1 text-center">
      <div id="home-header">
        <span className="build-with">Build with Claude</span>
      </div>

      <div
        className="description-text"
        style={{
        fontWeight: '400',
        fontSize: '20px',
        maxWidth: '42rem',
        textAlign: 'center',
        margin: '0 auto 1rem auto',
      }}
      >
        Learn how to get started with the Claude Developer Platform and Claude Code.
      </div>

      <div className="flex items-center justify-center">
        <button
          type="button"
          className="w-full flex items-center text-sm leading-6 rounded-lg mt-6 py-2.5 px-4 shadow-sm text-gray-400 bg-white dark:bg-white ring-1 ring-gray-400/20 hover:ring-gray-600/25 focus:outline-primary"
          id="home-search-entry"
          style={{
        maxWidth: '32rem',
      }}
          onClick={openSearch}
        >
          <span className="ml-[-0.3rem]">Ask Claude about docs...</span>
        </button>
      </div>
    </div>
  </div>
</div>

<div style={{ maxWidth: '70rem', marginLeft: 'auto', marginRight: 'auto', paddingLeft: '1.25rem', paddingRight: '1.25rem', marginTop: '3rem' }}>
  <h2 className="description-text" style={{ fontFamily: 'Copernicus, serif', fontWeight: '300', fontSize: '28px', marginBottom: '1.5rem', textAlign: 'center' }}>
    Claude Developer Platform
  </h2>

  <div className="home-cards-custom">
    <Card title="Get started" icon="play" href="/en/docs/get-started">
      Make your first API call in minutes.
    </Card>

    <Card title="Features overview" icon="brain-circuit" href="/en/api/overview">
      Explore the advanced features and capabilities now available in Claude.
    </Card>

    <Card title="What's new in Claude 4.5" icon="head-side-gear" href="/en/docs/about-claude/models/whats-new-claude-4-5">
      Discover the latest advancements in Claude 4.5 models, including Sonnet 4.5 and Haiku 4.5.
    </Card>

    <Card title="API reference" icon="code-simple" href="/en/api/overview">
      Integrate and scale using our API and SDKs.
    </Card>

    <Card title="Claude Console" icon="computer" href="https://console.anthropic.com">
      Craft and test powerful prompts directly in your browser.
    </Card>

    <Card title="Release notes" icon="star" href="/en/release-notes/api">
      Learn about changes and new features in the Claude Developer Platform.
    </Card>
  </div>
</div>

<div style={{ maxWidth: '70rem', marginLeft: 'auto', marginRight: 'auto', paddingLeft: '1.25rem', paddingRight: '1.25rem', marginTop: '3rem' }}>
  <h2 className="description-text" style={{ fontFamily: 'Copernicus, serif', fontWeight: '300', fontSize: '28px', marginBottom: '1.5rem', textAlign: 'center' }}>
    Claude Code
  </h2>

  <div className="home-cards-custom">
    <Card title="Claude Code quickstart" icon="square-terminal" href="https://code.claude.com/docs/en/quickstart">
      Get started with Claude Code.
    </Card>

    <Card title="Claude Code reference" icon="square-terminal" href="https://code.claude.com/docs/en/overview">
      Consult the Claude Code reference documentation for details on feature implementation and configuration.
    </Card>

    <Card title="Claude Code changelog" icon="star" href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">
      Learn about changes and new features in Claude Code.
    </Card>
  </div>
</div>

<div style={{ maxWidth: '70rem', marginLeft: 'auto', marginRight: 'auto', paddingLeft: '1.25rem', paddingRight: '1.25rem', marginTop: '3rem', marginBottom: '4rem' }}>
  <h2 className="description-text" style={{ fontFamily: 'Copernicus, serif', fontWeight: '300', fontSize: '28px', marginBottom: '1.5rem', textAlign: 'center' }}>
    Learning resources
  </h2>

  <div className="home-cards-custom">
    <Card title="Anthropic Courses" icon="graduation-cap" href="https://anthropic.skilljar.com/">
      Explore Anthropic's educational courses and projects.
    </Card>

    <Card title="Claude Cookbook" icon="utensils" href="https://github.com/anthropics/anthropic-cookbook">
      See replicable code samples and implementations.
    </Card>

    <Card title="Claude Quickstarts" icon="bolt-lightning" href="https://github.com/anthropics/anthropic-quickstarts">
      Deployable applications built with our API.
    </Card>
  </div>
</div>
