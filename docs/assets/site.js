const roleData = {
  it: {
    label: "IT Support Specialist who brings security discipline to every ticket.",
    summary:
      "3+ years of Tier 1-3 support across education and regulated healthcare. I resolve user, identity, endpoint, Microsoft 365, and access issues with clear documentation and dependable follow-through.",
    resume: "assets/resumes/Brian_Santiago_IT.pdf",
    resumeText: "Open IT Support resume",
    projectText: "View IT Support proof",
    tools: [
      "Microsoft 365",
      "Active Directory",
      "Entra ID",
      "ServiceNow",
      "NinjaOne",
      "Windows 10/11",
    ],
    proof: "3+ years of Tier 1-3 support across education and regulated healthcare.",
    boundary: "Professional experience",
    context: "Showing the strongest IT Support and identity evidence first.",
    title: "Brian Santiago | IT Support Portfolio",
  },
  soc: {
    label: "SOC Analyst candidate grounded in real support and identity operations.",
    summary:
      "Professional endpoint, account, and sign-in investigation experience supported by a documented Microsoft Sentinel authentication lab, KQL casebook, Defender review, and structured escalation notes.",
    resume: "assets/resumes/Brian_Santiago_SOC.pdf",
    resumeText: "Open SOC resume",
    projectText: "View SOC proof",
    tools: [
      "Microsoft Sentinel",
      "KQL",
      "Microsoft Defender",
      "Event Viewer",
      "Splunk",
      "MITRE ATT&CK",
    ],
    proof: "Professional endpoint and identity investigation plus documented SOC lab evidence.",
    boundary: "Professional bridge + hands-on lab",
    context: "Showing the strongest SOC investigation and escalation evidence first.",
    title: "Brian Santiago | SOC Analyst Portfolio",
  },
  grc: {
    label: "GRC Analyst candidate who turns technical work into reviewable evidence.",
    summary:
      "Professional compliance-support work across access, endpoint, change, and audit evidence, backed by clearly labeled synthetic exercises in access review, IAM lifecycle, risk, controls, policy, and third-party risk.",
    resume: "assets/resumes/Brian_Santiago_GRC.pdf",
    resumeText: "Open GRC resume",
    projectText: "View GRC proof",
    tools: [
      "NIST CSF",
      "ISO 27001",
      "HIPAA",
      "SOX ITGC",
      "Access Reviews",
      "TPRM",
    ],
    proof: "Professional compliance-support evidence plus clearly labeled synthetic GRC artifacts.",
    boundary: "Professional bridge + synthetic portfolio",
    context: "Showing the strongest access, risk, control, and audit evidence first.",
    title: "Brian Santiago | GRC Analyst Portfolio",
  },
};

const roleButtons = [...document.querySelectorAll("button[data-role]")];
const roleTitle = document.getElementById("role-title");
const roleSummary = document.getElementById("role-summary");
const roleResume = document.getElementById("role-resume");
const roleTools = document.getElementById("role-tools");
const roleProof = document.getElementById("role-proof");
const roleBoundary = document.getElementById("role-boundary");
const projectContext = document.getElementById("project-context");
const projectGrid = document.getElementById("project-grid");
const projectCards = [...document.querySelectorAll(".project-card")];
const skillGroups = [...document.querySelectorAll("[data-skill-roles]")];
const resumeCards = [...document.querySelectorAll("[data-resume-role]")];
const projectAction = document.querySelector(".hero-actions a[href='#projects']");

function validRole(role) {
  return Object.prototype.hasOwnProperty.call(roleData, role) ? role : "it";
}

function replaceList(target, values) {
  if (!target) return;
  target.replaceChildren(
    ...values.map((value) => {
      const item = document.createElement("li");
      item.textContent = value;
      return item;
    }),
  );
}

function sortProjects(role) {
  if (!projectGrid) return;
  const rankKey = `rank${role.charAt(0).toUpperCase()}${role.slice(1)}`;
  const sorted = [...projectCards].sort((left, right) => {
    const leftRank = Number(left.dataset[rankKey] || 99);
    const rightRank = Number(right.dataset[rankKey] || 99);
    return leftRank - rightRank;
  });

  sorted.forEach((card, index) => {
    card.classList.toggle("is-priority", index < 2);
    projectGrid.append(card);
  });
}

function updateUrl(role) {
  const url = new URL(window.location.href);
  url.searchParams.set("role", role);
  history.replaceState({ role }, "", `${url.pathname}${url.search}${url.hash}`);
}

function applyRole(requestedRole, options = {}) {
  const role = validRole(requestedRole);
  const data = roleData[role];

  document.body.dataset.activeRole = role;
  document.title = data.title;

  roleButtons.forEach((button) => {
    button.setAttribute("aria-pressed", String(button.dataset.role === role));
  });

  if (roleTitle) roleTitle.textContent = data.label;
  if (roleSummary) roleSummary.textContent = data.summary;
  if (roleResume) {
    roleResume.href = data.resume;
    roleResume.textContent = data.resumeText;
  }
  if (projectAction) projectAction.textContent = data.projectText;
  if (roleProof) roleProof.textContent = data.proof;
  if (roleBoundary) roleBoundary.textContent = data.boundary;
  if (projectContext) projectContext.textContent = data.context;
  replaceList(roleTools, data.tools);

  skillGroups.forEach((group) => {
    const roles = (group.dataset.skillRoles || "").split(/\s+/);
    group.hidden = !roles.includes(role);
  });

  resumeCards.forEach((card) => {
    card.classList.toggle("is-selected", card.dataset.resumeRole === role);
  });

  sortProjects(role);
  if (options.updateUrl !== false) updateUrl(role);
}

roleButtons.forEach((button) => {
  button.addEventListener("click", () => applyRole(button.dataset.role || "it"));
});

window.addEventListener("popstate", () => {
  const role = new URLSearchParams(window.location.search).get("role") || "it";
  applyRole(role, { updateUrl: false });
});

async function copyEmail() {
  const status = document.getElementById("copy-status");
  const email = "briand.santiago@gmail.com";

  if (status) status.textContent = "Copying...";

  try {
    if (!navigator.clipboard?.writeText) throw new Error("Clipboard API unavailable");
    await Promise.race([
      navigator.clipboard.writeText(email),
      new Promise((_, reject) => {
        window.setTimeout(() => reject(new Error("Clipboard request timed out")), 600);
      }),
    ]);
    if (status) status.textContent = "Email copied";
  } catch (error) {
    const input = document.createElement("textarea");
    input.value = email;
    input.setAttribute("readonly", "");
    input.style.position = "fixed";
    input.style.opacity = "0";
    document.body.append(input);
    input.select();
    const copied = document.execCommand("copy");
    input.remove();

    if (copied) {
      if (status) status.textContent = "Email copied";
      return;
    }

    const selection = window.getSelection();
    const emailLink = document.querySelector(`a[href='mailto:${email}'] strong`);
    if (selection && emailLink) {
      const range = document.createRange();
      range.selectNodeContents(emailLink);
      selection.removeAllRanges();
      selection.addRange(range);
    }
    if (status) status.textContent = "Select the email address above";
  }
}

document.getElementById("copy-email")?.addEventListener("click", copyEmail);

const initialRole = new URLSearchParams(window.location.search).get("role") || "it";
applyRole(initialRole);
