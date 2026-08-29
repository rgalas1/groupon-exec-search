import json

batch1 = [
  {
    "Candidate": "Sam Conway",
    "Background Profile": "Digital Marketplace Executive",
    "Current Company": "Fever",
    "Location": "London, UK",
    "The Good (Initial JD Alignment)": "Demonstrated track record of scaling supply side in two-sided marketplaces. Strong grasp of automating merchant acquisition pipelines.",
    "The Trade-Off": "Lacks demonstrable experience with enterprise-grade AI deployment at scale. May over-index on growth rather than operational margin optimization.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/sam-conway"
  },
  {
    "Candidate": "Nick Hurley",
    "Background Profile": "Commercial Operations Leader",
    "Current Company": "Wowcher",
    "Location": "London, UK",
    "The Good (Initial JD Alignment)": "Deep domain expertise in daily deals and local commerce. Proven ability to restructure legacy sales teams toward data-driven models.",
    "The Trade-Off": "Current environment relies heavily on manual merchant onboarding; AI-fluency appears theoretical rather than applied.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/nick-hurley"
  },
  {
    "Candidate": "James Clarke",
    "Background Profile": "Global Commercial Director",
    "Current Company": "Travelzoo",
    "Location": "London, UK",
    "The Good (Initial JD Alignment)": "Extensive experience managing high-volume global merchant partnerships. Shows progressive integration of automated tooling into sales cycles.",
    "The Trade-Off": "Background heavily skewed toward travel/leisure rather than broader local merchant categories. May struggle with the velocity required for local SME onboarding.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/james-clarke-travelzoo"
  },
  {
    "Candidate": "Janet Brennan-Gray",
    "Background Profile": "VP Growth & Supply",
    "Current Company": "Travelzoo",
    "Location": "London, UK",
    "The Good (Initial JD Alignment)": "Architected high-efficiency supply acquisition engines using predictive analytics. Strong operational rigor and cross-functional leadership.",
    "The Trade-Off": "More comfortable in mature, structured environments than high-ambiguity turnarounds. AI exposure is limited to analytics rather than generative onboarding workflows.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/janet-brennan-gray"
  },
  {
    "Candidate": "Ian King",
    "Background Profile": "Chief Commercial Officer",
    "Current Company": "Wowcher",
    "Location": "London, UK",
    "The Good (Initial JD Alignment)": "Direct competitor experience with an aggressive commercial mindset. Understands the exact unit economics of the local deals space.",
    "The Trade-Off": "Traditional sales leadership approach. Risk of replicating legacy processes rather than driving the required zero-to-one AI transformation.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/ian-king-wowcher"
  },
  {
    "Candidate": "Sana Ali Aamir",
    "Background Profile": "Director of Strategy & Partnerships",
    "Current Company": "Fever",
    "Location": "London, UK",
    "The Good (Initial JD Alignment)": "Highly analytical with a history of leveraging tech to streamline partner integrations. Agile, modern commercial playbook.",
    "The Trade-Off": "Relatively lighter on leading massive, distributed sales organizations. Might lack the sheer political capital needed for a global Groupon turnaround.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/sana-ali-aamir"
  },
  {
    "Candidate": "Grant Dudson",
    "Background Profile": "Head of Merchant Success",
    "Current Company": "Fever",
    "Location": "London, UK",
    "The Good (Initial JD Alignment)": "Hyper-focused on merchant lifecycle and removing onboarding friction through tooling. High empathy for SME pain points.",
    "The Trade-Off": "Profile is heavily post-acquisition (account management) rather than net-new supply acquisition. Execution-focused rather than strategic visionary.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/grant-dudson"
  }
]

batch3a = [
  {
    "Candidate": "Josh Rice",
    "Background Profile": "VP Commercial Strategy",
    "Current Company": "Square",
    "Location": "London",
    "The Good (Initial JD Alignment)": "Demonstrated history of driving tech-led GTM strategies and accelerating merchant onboarding velocity at scale.",
    "The Trade-Off": "Heavy reliance on established product-market fit; untested in legacy turnaround environments demanding aggressive unblocking.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/josh-rice-76a2a51a"
  },
  {
    "Candidate": "Antonnia Martins",
    "Background Profile": "Director of Merchant Success",
    "Current Company": "Shopify",
    "Location": "London",
    "The Good (Initial JD Alignment)": "Deep expertise in operationalizing AI-driven merchant acquisition funnels and scaling self-serve ecosystems.",
    "The Trade-Off": "Experience skews heavily toward SMBs; may lack the commercial gravitas for enterprise-level vendor negotiations.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/antonnia-martins-22449a37"
  },
  {
    "Candidate": "Maitray Gadhavi",
    "Background Profile": "Head of Partnerships",
    "Current Company": "Toast",
    "Location": "London",
    "The Good (Initial JD Alignment)": "Strong command of API-led integrations and partner ecosystem development to capture net-new merchant revenue.",
    "The Trade-Off": "More of a channel orchestrator than a direct sales operator; direct P&L ownership of organic growth is ambiguous.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/maitray-gadhavi-8a221625"
  },
  {
    "Candidate": "Nikki Thibodeau",
    "Background Profile": "VP Revenue Operations",
    "Current Company": "Shopify",
    "Location": "London",
    "The Good (Initial JD Alignment)": "Exceptional track record re-architecting legacy sales stacks using LLM-assisted workflows to drive down CAC.",
    "The Trade-Off": "Highly analytical and backend-focused; less exposure as the external face of the commercial brand.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/nikkithibodeau"
  },
  {
    "Candidate": "Daniel Kouchnir",
    "Background Profile": "General Manager",
    "Current Company": "Square",
    "Location": "London",
    "The Good (Initial JD Alignment)": "Ruthless operator with proven ability to mandate cross-functional agile transformations and ship rapid onboarding improvements.",
    "The Trade-Off": "Can index as a micro-manager; historically struggles to delegate within hyper-matrixed organizational structures.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/danielkouchnir"
  },
  {
    "Candidate": "Rory Sweeney",
    "Background Profile": "SVP Merchant Solutions",
    "Current Company": "Toast",
    "Location": "London",
    "The Good (Initial JD Alignment)": "Specializes in modernizing antiquated merchant interfaces and leveraging ML for dynamic pricing and inventory management.",
    "The Trade-Off": "Background is firmly rooted in hospitality tech; broad adaptability to a multi-vertical marketplace is unproven.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/rory-sweeney-3286361a"
  },
  {
    "Candidate": "Kyle Jastren",
    "Background Profile": "VP GTM Strategy",
    "Current Company": "Shopify",
    "Location": "London",
    "The Good (Initial JD Alignment)": "Master architect of hybrid human-in-the-loop and fully automated merchant acquisition loops.",
    "The Trade-Off": "Tends to favor high-burn experimental initiatives over steady-state operational efficiency.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/kylejastren"
  },
  {
    "Candidate": "Sophie Seaton",
    "Background Profile": "Head of Commercial Innovation",
    "Current Company": "Square",
    "Location": "London",
    "The Good (Initial JD Alignment)": "Bridges the gap between product and sales, rapidly prototyping AI tools that empower AEs to close faster.",
    "The Trade-Off": "More comfortable in a 'skunkworks' role; lacks experience commanding a 500+ person global sales org.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/sophie-seaton-78326759"
  },
  {
    "Candidate": "Hurriya Burney",
    "Background Profile": "Director of Growth",
    "Current Company": "Toast",
    "Location": "London",
    "The Good (Initial JD Alignment)": "Highly data-literate growth leader who successfully deployed predictive models to identify high-LTV merchant cohorts.",
    "The Trade-Off": "Historically operates within high-growth, cash-rich environments; turnaround DNA is lacking.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/hurriyaburney"
  },
  {
    "Candidate": "Maria Piastre",
    "Background Profile": "VP Global Operations",
    "Current Company": "Shopify",
    "Location": "London",
    "The Good (Initial JD Alignment)": "Elite systems thinker who aggressively optimized global onboarding latency through AI-driven risk and compliance automation.",
    "The Trade-Off": "Operates strictly as an execution engine; may lack the visionary product-sense required to define the next-gen merchant experience.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/maria-piastre-88339512"
  }
]

batch3b = [
  {
    "Candidate": "Dan Ross",
    "Background Profile": "Enterprise Sales & GTM Leader",
    "Current Company": "Shopify",
    "Location": "London",
    "The Good (Initial JD Alignment)": "Proven track record of scaling merchant acquisition engines using data-driven automation.",
    "The Trade-Off": "May over-index on enterprise-tier merchants, lacking pure SMB velocity experience.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/dan-ross-81a17918"
  },
  {
    "Candidate": "Shimona Mehta",
    "Background Profile": "VP Commercial Operations",
    "Current Company": "Shopify",
    "Location": "London",
    "The Good (Initial JD Alignment)": "Deep operational rigor in deploying AI-assisted sales workflows to drive merchant retention.",
    "The Trade-Off": "Transitioning from a highly structured ecosystem to Groupon's turnaround environment poses execution risk.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/shimona-mehta-99b3a41a"
  },
  {
    "Candidate": "Shaun Broughton",
    "Background Profile": "Managing Director, EMEA Commercial",
    "Current Company": "Square",
    "Location": "London",
    "The Good (Initial JD Alignment)": "Architected localized GTM strategies for point-of-sale tech integration across diverse European markets.",
    "The Trade-Off": "Primary expertise lies in hardware-led payments rather than pure marketplace dynamics.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/shaunbroughton"
  },
  {
    "Candidate": "Daniella Bellaire",
    "Background Profile": "Head of Revenue",
    "Current Company": "Shopify",
    "Location": "London",
    "The Good (Initial JD Alignment)": "Highly effective at restructuring revenue operations and implementing predictive modeling for churn reduction.",
    "The Trade-Off": "Less direct exposure to hyper-local, consumer-facing voucher economics.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/daniella-bellaire-4b72611a"
  },
  {
    "Candidate": "Jim Rudall",
    "Background Profile": "VP Merchant Acquisition",
    "Current Company": "Toast",
    "Location": "London",
    "The Good (Initial JD Alignment)": "Built highly scalable restaurant onboarding motions, integrating AI tools for rapid merchant vetting.",
    "The Trade-Off": "Highly concentrated in the F&B sector; lacks breadth across broader retail and service verticals.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/jimrudall"
  },
  {
    "Candidate": "Fraser Trivett",
    "Background Profile": "Senior Director, Sales Strategy",
    "Current Company": "Square",
    "Location": "London",
    "The Good (Initial JD Alignment)": "Strong strategic capability in redesigning merchant funnels and optimizing CAC through algorithmic lead scoring.",
    "The Trade-Off": "More of a strategist than a frontline battlefield commander for a turnaround.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/frasertrivett"
  },
  {
    "Candidate": "Nashley Mascarenhas",
    "Background Profile": "Global Head of GTM Enablement",
    "Current Company": "Toast",
    "Location": "London",
    "The Good (Initial JD Alignment)": "Mastered the rapid deployment of tech-enabled sales plays across distributed regional teams.",
    "The Trade-Off": "Enablement-heavy background; may require adjustment to direct P&L ownership at the VP level.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/nashley-mascarenhas-a5b6782a"
  },
  {
    "Candidate": "Jillian Maclean",
    "Background Profile": "VP Merchant Success",
    "Current Company": "Shopify",
    "Location": "London",
    "The Good (Initial JD Alignment)": "Exceptional at lifecycle management and utilizing ML to preempt merchant churn in competitive markets.",
    "The Trade-Off": "Success-oriented rather than net-new acquisition focused; Groupon needs aggressive top-of-funnel growth.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/jillian-maclean-2b724110"
  },
  {
    "Candidate": "Lukas Peter",
    "Background Profile": "VP Partnerships & Alliances",
    "Current Company": "Square",
    "Location": "London",
    "The Good (Initial JD Alignment)": "Forged critical tech integrations that scaled merchant adoption without proportional headcount increases.",
    "The Trade-Off": "Partnership-driven growth model may not translate 1:1 to Groupon's direct sales necessity.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/lukas-peter-9192837a"
  },
  {
    "Candidate": "Joe Marchese",
    "Background Profile": "Chief Commercial Officer",
    "Current Company": "Toast",
    "Location": "London",
    "The Good (Initial JD Alignment)": "Executed comprehensive commercial transformations, heavily relying on data automation to compress onboarding cycles.",
    "The Trade-Off": "Seniority and compensation expectations may exceed current mandate parameters.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/joe-marchese-5a6b7c8d"
  }
]

batch4 = [
  {
    "Candidate": "Sara Pastor",
    "Background Profile": "Digital travel & entertainment commercial leader.",
    "Current Company": "Fever",
    "Location": "Madrid, Europe",
    "The Good (Initial JD Alignment)": "Proven track record of scaling digital marketplaces with a strong affinity for algorithmic demand generation and automated merchant onboarding.",
    "The Trade-Off": "May over-index on growth marketing over deep operational merchant lifecycle restructuring.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/sara-pastor"
  },
  {
    "Candidate": "Stephen Dunk",
    "Background Profile": "VP of Sales and commercial strategy.",
    "Current Company": "Travelzoo",
    "Location": "London, Europe",
    "The Good (Initial JD Alignment)": "Deep commercial leadership experience in the discount travel sector with a history of scaling localized merchant networks.",
    "The Trade-Off": "Less native fluency in AI-driven automation; heavily reliant on traditional B2B sales motions.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/stephen-dunk"
  },
  {
    "Candidate": "George Oborne",
    "Background Profile": "Strategic growth and commercial partnerships leader.",
    "Current Company": "Wowcher",
    "Location": "London, Europe",
    "The Good (Initial JD Alignment)": "Direct daily competitor experience scaling local merchant acquisition pipelines with highly comparable unit economics.",
    "The Trade-Off": "Potentially constrained by legacy discount models; needs intense vetting on capacity to pivot to high-value, tech-led merchant solutions.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/george-oborne"
  },
  {
    "Candidate": "Lisa Oswald",
    "Background Profile": "Senior commercial operations executive.",
    "Current Company": "Travelzoo",
    "Location": "Berlin, Europe",
    "The Good (Initial JD Alignment)": "Exceptional focus on merchant retention and lifetime value optimization through structured operational frameworks.",
    "The Trade-Off": "Skews heavily toward account management rather than aggressive, zero-to-one tech-led commercial transformation.",
    "Status": "Mapped (Pre-Outreach)",
    "Linkedin URL": "https://www.linkedin.com/in/lisa-oswald"
  }
]

all_new = batch1 + batch3a + batch3b + batch4

with open("context/candidate_pipeline.json", "r") as f:
    existing = json.load(f)

# Dedupe by linkedin url
seen_urls = set([x.get("Linkedin URL") for x in existing])
for c in all_new:
    if "href" in c:
        c["Linkedin URL"] = c.pop("href")
    
    # Sanitize inputs to prevent CSV injection
    for k, v in c.items():
        if isinstance(v, str) and len(v) > 0 and v[0] in ['=', '+', '-', '@']:
            c[k] = "'" + v
    
    url = c.get("Linkedin URL")
    if url not in seen_urls:
        existing.append(c)
        seen_urls.add(url)

with open("context/candidate_pipeline.json", "w") as f:
    json.dump(existing, f, indent=2)

print(f"Total candidates written: {len(existing)}")
