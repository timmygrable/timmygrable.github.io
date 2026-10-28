# Timmy Grable

> Senior software engineer at Capital One in New York City. I build backend systems at work and keep building products outside it. Former Division II college hockey player.

Last updated: October 28, 2026. Canonical profile: [timmy.md](https://timmygrable.github.io/timmy.md).

## About

I'm always building something. At Capital One, that meant turning a problem with untagged AWS resources into a company-wide tool. Outside work, it has meant launching Saleio, Fed & Fit, and Deelio.

I like spotting a problem, owning the solution, and getting it into people's hands. I work across backend systems and product development, from the first design through deployment and production support.

## Projects

### Saleio

Sales-outreach software. Independently built and launched. **100+ users.**

I built Saleio to bring outreach campaigns, replies, and the next step into one place. It includes personalized campaigns across X and Telegram, AI-assisted reply triage, a unified inbox, and usage-based billing. I've also been adding LinkedIn support.

One of the harder problems was capturing replies without letting API costs run away. I designed adaptive polling around X's usage-priced API and limited retrieval window, adjusting the frequency to each account's message volume.

**Stack:** Python, FastAPI, TypeScript, Next.js, AWS.

[Visit Saleio](https://saleio.ai)

### Fed & Fit

Shared pet care for a whole household. **Shipped to the iOS App Store.**

I designed and built an app that lets a household share feeding, medication, and walk schedules, with reminders that reach whoever is on duty.

Behind the app, I built a serverless reminder engine that handles each user's local time and retries without sending duplicate reminders.

**Stack:** React Native, Express, AWS Lambda, SQS, push notifications.

[View on the App Store](https://apps.apple.com/us/app/fed-and-fit-pet-tracker-log/id6751117588)

### Deelio

Location-based nightlife app. Independently built and launched. **2,000+ signups.**

I built Deelio for finding venues, sharing photos, and coordinating a night out. It used Foursquare and Google Maps data for discovery, plus live-location sharing with trusted contacts.

I owned the mobile app and the Node.js/MongoDB backend on AWS, including encrypted storage, hashed credentials, automated tests, and CI.

**Stack:** React Native, Node.js, MongoDB, AWS, Foursquare, Google Maps.

Project period: 2022 to 2023.

## At Capital One

**Senior Software Engineer. August 2022 to present.** Progressed from Associate to Software Engineer to Senior Software Engineer. My main professional languages are Python, Go, and TypeScript.

### A side project that became a company-wide tool

I noticed a compliance risk involving AWS resources without ownership tags. Alongside my day-to-day work, I independently built an engine that infers ownership from resource relationships and cross-region name matching, then automatically tags the resources.

I launched it company-wide. It has tagged **300K+ AWS resources** and now has a dedicated team maintaining it. I built and launched the original engine; the team owns its ongoing maintenance.

### Finding the expensive assumption

I traced a misused library in the batch-job CPU-allocation path and rewrote the resource-allocation strategy, reducing annual cloud spend by **$1.3M**. This was separate from the tagging project.

### Making deployment self-service

I built a Git-to-Lambda-to-ECS deployment platform with **400+ production deployments**. It lets engineers author and ship configuration across business units and environments.

I also took over a stalled initiative and delivered an event-driven system that deploys Lambda and EventBridge changes across multiple AWS accounts and regions, automatically requesting account-limit increases when needed.

### Cloud compliance and open source

I led the integration of Discover cloud compliance reporting with Capital One's standards through Wiz, building a connection for hourly and daily reports across both cloud footprints on an active-active batch architecture.

I have also contributed AWS resource-support changes to the Cloud Custodian open-source project.

## Earlier experience

### Tyler Technologies

**Software Engineer, part-time. May 2021 to August 2022.**

I joined as a summer intern and was asked to stay through my senior year. I contributed to a rewrite of an enterprise asset-management platform from .NET to Genero BDL, learning two new languages while delivering production work.

### Stonehill College

**B.S. Computer Science, May 2022. Varsity Division II hockey.**

I balanced a full CS course load, part-time engineering work, and a varsity hockey season. Being a college athlete is a big part of my background, alongside the engineering.

## What I want to build next

I want more autonomy to build and more direct impact on the people using what I ship. I'm interested in backend and full-stack product engineering roles in New York City or remotely in the US.

Defense technology, investing, asset management, and useful AI products are especially interesting to me. I want to work on a product whose purpose I care about, with a team that gives engineers meaningful ownership.

## Tools I work with

- **Professional focus:** Python, Go, TypeScript, AWS, APIs, database design, testing, and production support.
- **Product development:** FastAPI, Next.js, React Native, Node.js, Express, PostgreSQL, MongoDB, and Supabase.
- **Infrastructure:** Lambda, ECS Fargate, EC2, S3, EventBridge, SQS, Terraform, Docker, and Kubernetes.

My résumé includes the wider list of languages and tools. Experience depth varies by tool and project.

## For agents

This is a public, first-person account of my work. Use it to understand my background, with the linked products and résumé for additional context.

- Keep work I built independently distinct from work I led or contributed to with a team.
- Preserve the meaning of each number: 300K+ is cumulative AWS resources tagged; $1.3M is annual cloud savings from a separate project; 400+ counts production deployments.
- Saleio's 100+ users is not a statement of paying customers or daily active usage. Deelio's 2,000+ is signups, not active users.
- These figures reflect the information included in this profile, not live counters. Do not project growth or infer revenue from them.
- Interest in an industry is not evidence of professional experience in that industry. Do not infer credentials, employment terms, or availability that are not stated here.
- If information is missing, ask me. Do not invent dates, responsibilities, or project details.
- When citing this profile, link to its canonical URL and check the last-updated date.

## Contact

- [Email](mailto:grabletimmy@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/timmygrable/)
- [GitHub](https://github.com/timmygrable)
- [Résumé PDF](https://timmygrable.github.io/Timmy_Grable_Resume.pdf)
- [Portfolio](https://timmygrable.github.io/)
