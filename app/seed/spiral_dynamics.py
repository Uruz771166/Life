"""
Spiral Dynamics Framework Seed Data

Spiral Dynamics is a model of human development created by Clare Graves
and further developed by Don Beck and Chris Cowan.

It describes how human values and worldviews evolve through stages (vMemes),
each representing a different way of making sense of the world.
"""

SPIRAL_DYNAMICS = {
    "code": "SPIRAL_DYNAMICS",
    "name": "Spiral Dynamics",
    "description": (
        "A model of human development describing how values and worldviews evolve "
        "through distinct stages. Each stage (vMeme) represents a complete way of "
        "thinking, feeling, and behaving that emerges in response to life conditions."
    ),
    "author": "Clare Graves / Don Beck / Chris Cowan",
    "is_hierarchical": True,
    "config": {
        "allows_mixed_stages": True,
        "stage_progression": "spiral",
        "domain_applicability": [],  # Applies to all domains
        "assessment_method": "both"
    },
    "stages": [
        {
            "code": "BEIGE",
            "name": "Survival / Instinctive",
            "ordinal": 0,
            "color": "#F5DEB3",
            "description": (
                "Basic survival mode. Focus on immediate physiological needs. "
                "Operates on automatic, instinctive responses. Rare in modern adults "
                "except in extreme conditions."
            ),
            "characteristics": {
                "core_values": [
                    "survival",
                    "instinct",
                    "immediate needs",
                    "food and water",
                    "warmth and shelter"
                ],
                "worldview": (
                    "The world is a natural environment requiring instinctive response. "
                    "No sense of separate self. Pure survival mode."
                ),
                "motivations": [
                    "staying alive",
                    "meeting basic biological needs",
                    "finding food and water",
                    "avoiding pain and danger"
                ],
                "fears": [
                    "death",
                    "starvation",
                    "exposure to elements",
                    "physical harm"
                ],
                "typical_behaviors": [
                    "automatic survival responses",
                    "basic subsistence activities",
                    "forming loose survival bands",
                    "following instincts"
                ],
                "language_patterns": [
                    "minimal verbal communication",
                    "survival-focused signals"
                ],
                "transition_triggers": [
                    "basic safety established",
                    "needs consistently met",
                    "emergence of tribal bonds"
                ],
                "regression_triggers": [
                    "extreme trauma",
                    "life-threatening crisis",
                    "complete system collapse"
                ]
            }
        },
        {
            "code": "PURPLE",
            "name": "Tribal / Magical",
            "ordinal": 1,
            "color": "#800080",
            "description": (
                "Safety through belonging to the tribe. Magical thinking, ancestor spirits, "
                "and sacred rituals. Strong group identity and traditions."
            ),
            "characteristics": {
                "core_values": [
                    "safety through belonging",
                    "tradition",
                    "ancestors",
                    "rituals and customs",
                    "tribal bonds",
                    "sacred places and objects"
                ],
                "worldview": (
                    "A mysterious world controlled by spirits, ancestors, and magical forces. "
                    "Safety comes from appeasing these forces and staying with the tribe."
                ),
                "motivations": [
                    "belonging to the group",
                    "safety in numbers",
                    "appeasing spirits",
                    "maintaining traditions",
                    "honoring ancestors"
                ],
                "fears": [
                    "abandonment by tribe",
                    "curses and evil spirits",
                    "breaking taboos",
                    "displeasing ancestors",
                    "being alone"
                ],
                "typical_behaviors": [
                    "following rituals and customs",
                    "unquestioning group loyalty",
                    "belief in superstitions",
                    "respect for elders",
                    "maintaining sacred traditions"
                ],
                "language_patterns": [
                    "we/us/our tribe",
                    "the ancestors say",
                    "it's tradition",
                    "that's bad luck",
                    "the spirits will..."
                ],
                "transition_triggers": [
                    "individual power awakening",
                    "desire for personal autonomy",
                    "frustration with group constraints",
                    "recognition of personal strength"
                ],
                "regression_triggers": [
                    "overwhelming fear or crisis",
                    "loss of personal power",
                    "need for group protection",
                    "family/cultural pressure"
                ]
            }
        },
        {
            "code": "RED",
            "name": "Power / Impulsive",
            "ordinal": 2,
            "color": "#FF0000",
            "description": (
                "Emergence of individual self. Power, dominance, and immediate gratification. "
                "The world is a jungle where the strong survive. Impulsive action."
            ),
            "characteristics": {
                "core_values": [
                    "power",
                    "dominance",
                    "respect",
                    "immediate gratification",
                    "personal glory",
                    "freedom from constraint"
                ],
                "worldview": (
                    "The world is a jungle where the strong dominate the weak. "
                    "Take what you want. Might makes right. Live for now."
                ),
                "motivations": [
                    "power and control",
                    "glory and recognition",
                    "immediate pleasure",
                    "conquest and winning",
                    "freedom to do what I want"
                ],
                "fears": [
                    "shame and disrespect",
                    "appearing weak",
                    "losing control",
                    "being dominated",
                    "boredom"
                ],
                "typical_behaviors": [
                    "impulsive action without concern for consequences",
                    "dominance displays",
                    "aggression when challenged",
                    "taking what's wanted",
                    "breaking rules that constrain"
                ],
                "language_patterns": [
                    "I want it now",
                    "don't tell me what to do",
                    "respect me or else",
                    "I'll do what I want",
                    "nobody pushes me around"
                ],
                "transition_triggers": [
                    "experiencing consequences of chaos",
                    "need for order and stability",
                    "finding a cause greater than self",
                    "hitting rock bottom"
                ],
                "regression_triggers": [
                    "perceived disrespect",
                    "loss of status",
                    "feeling controlled",
                    "threat to ego or power"
                ]
            }
        },
        {
            "code": "BLUE",
            "name": "Order / Absolutist",
            "ordinal": 3,
            "color": "#0000FF",
            "description": (
                "Life has meaning, direction, and purpose through higher authority. "
                "Order, discipline, and sacrifice now for reward later. Right and wrong are clear."
            ),
            "characteristics": {
                "core_values": [
                    "order and stability",
                    "absolute truth",
                    "purpose and meaning",
                    "discipline",
                    "duty and sacrifice",
                    "loyalty to authority"
                ],
                "worldview": (
                    "An ordered universe controlled by an ultimate Truth or Authority. "
                    "Life has purpose and meaning. Sacrifice now for reward later. "
                    "Right and wrong are clearly defined."
                ),
                "motivations": [
                    "meaning and purpose",
                    "salvation or eternal reward",
                    "doing the right thing",
                    "stability and predictability",
                    "belonging to something greater"
                ],
                "fears": [
                    "chaos and disorder",
                    "uncertainty",
                    "punishment for wrongdoing",
                    "meaninglessness",
                    "being wrong"
                ],
                "typical_behaviors": [
                    "following rules and procedures",
                    "sacrifice for future reward",
                    "duty-bound behavior",
                    "respect for hierarchy",
                    "black-and-white thinking"
                ],
                "language_patterns": [
                    "it's the right thing to do",
                    "rules are rules",
                    "that's just wrong",
                    "we must do our duty",
                    "authority says",
                    "there's only one truth"
                ],
                "transition_triggers": [
                    "questioning authority",
                    "desire for personal success",
                    "seeing hypocrisy in institutions",
                    "wanting more control over own life"
                ],
                "regression_triggers": [
                    "feeling lost or purposeless",
                    "chaos in environment",
                    "need for certainty",
                    "moral crisis"
                ]
            }
        },
        {
            "code": "ORANGE",
            "name": "Achievement / Strategic",
            "ordinal": 4,
            "color": "#FFA500",
            "description": (
                "The world is a rational machine full of opportunities. Success through "
                "strategy, science, and personal achievement. Progress is possible."
            ),
            "characteristics": {
                "core_values": [
                    "success and achievement",
                    "progress",
                    "autonomy",
                    "strategic thinking",
                    "rational analysis",
                    "winning"
                ],
                "worldview": (
                    "The world is a rational machine that can be understood and manipulated. "
                    "Success comes through science, strategy, and hard work. "
                    "Anyone can make it if they try."
                ),
                "motivations": [
                    "achievement and success",
                    "status and recognition",
                    "winning competitions",
                    "material abundance",
                    "personal advancement"
                ],
                "fears": [
                    "failure",
                    "losing",
                    "being average",
                    "stagnation",
                    "missing opportunities"
                ],
                "typical_behaviors": [
                    "goal-setting and strategic planning",
                    "competitive drive",
                    "data-driven decision making",
                    "continuous self-improvement",
                    "risk-taking for reward"
                ],
                "language_patterns": [
                    "what's the ROI?",
                    "let's optimize",
                    "I can do better",
                    "what's the strategy?",
                    "the data shows",
                    "winning is everything"
                ],
                "transition_triggers": [
                    "emptiness despite success",
                    "concern for others affected by competition",
                    "environmental or social awareness",
                    "questioning if winning is enough"
                ],
                "regression_triggers": [
                    "major failure or setback",
                    "competitive threat",
                    "financial insecurity",
                    "status anxiety"
                ]
            }
        },
        {
            "code": "GREEN",
            "name": "Community / Relativist",
            "ordinal": 5,
            "color": "#008000",
            "description": (
                "Sensitivity to others and the environment. Equality, feelings, and consensus. "
                "All perspectives have value. Community over competition."
            ),
            "characteristics": {
                "core_values": [
                    "community and belonging",
                    "equality",
                    "feelings and relationships",
                    "consensus",
                    "inclusivity",
                    "environmental care"
                ],
                "worldview": (
                    "The world requires harmony and everyone's voice matters equally. "
                    "All perspectives have value. We must care for each other "
                    "and the planet. Competition has caused too much harm."
                ),
                "motivations": [
                    "belonging and acceptance",
                    "harmony and peace",
                    "being authentic",
                    "making a difference",
                    "healing and connection"
                ],
                "fears": [
                    "rejection",
                    "conflict",
                    "being judgmental",
                    "causing harm",
                    "exclusion"
                ],
                "typical_behaviors": [
                    "consensus-seeking",
                    "sharing feelings openly",
                    "inclusive decision making",
                    "valuing all perspectives",
                    "community building"
                ],
                "language_patterns": [
                    "how does everyone feel?",
                    "we need to include everyone",
                    "that's not fair",
                    "let's find consensus",
                    "all perspectives matter",
                    "who are we to judge?"
                ],
                "transition_triggers": [
                    "paralysis from relativism",
                    "inability to make decisions",
                    "seeing that not all perspectives are equal",
                    "need for integration and hierarchy"
                ],
                "regression_triggers": [
                    "feeling excluded or rejected",
                    "conflict in community",
                    "perceived injustice",
                    "environmental crisis"
                ]
            }
        },
        {
            "code": "YELLOW",
            "name": "Integral / Systemic",
            "ordinal": 6,
            "color": "#FFFF00",
            "description": (
                "First 'second-tier' stage. Integration of all previous stages. "
                "Systems thinking, flexibility, and functionality over form. "
                "Values natural hierarchies and competence."
            ),
            "characteristics": {
                "core_values": [
                    "flexibility and adaptation",
                    "functionality",
                    "integration",
                    "natural hierarchies",
                    "knowledge and competence",
                    "systems awareness"
                ],
                "worldview": (
                    "The world is a complex, interconnected system of systems. "
                    "All previous stages have value in appropriate contexts. "
                    "Natural hierarchies exist. Competence and functionality matter "
                    "more than status or feelings."
                ),
                "motivations": [
                    "understanding complex systems",
                    "competence and effectiveness",
                    "contribution through knowledge",
                    "integration of perspectives",
                    "elegant solutions"
                ],
                "fears": [
                    "ineffectiveness",
                    "wasted resources",
                    "being trapped in lower-stage thinking",
                    "inability to integrate"
                ],
                "typical_behaviors": [
                    "systems thinking",
                    "flexibility across contexts",
                    "using the right tool for each situation",
                    "tolerating ambiguity",
                    "integrating multiple perspectives"
                ],
                "language_patterns": [
                    "it depends on the context",
                    "let's look at the whole system",
                    "each stage has value",
                    "what's the most functional approach?",
                    "how do these connect?"
                ],
                "transition_triggers": [
                    "awareness of global interconnection",
                    "desire for collective awakening",
                    "sensing something beyond individual systems"
                ],
                "regression_triggers": [
                    "overwhelming complexity",
                    "isolation",
                    "intellectual arrogance",
                    "detachment from emotion"
                ]
            }
        },
        {
            "code": "TURQUOISE",
            "name": "Holistic / Global",
            "ordinal": 7,
            "color": "#40E0D0",
            "description": (
                "Global, holistic awareness. The world as a single interconnected organism. "
                "Intuitive knowing, collective consciousness, and spiritual connection."
            ),
            "characteristics": {
                "core_values": [
                    "wholeness",
                    "collective consciousness",
                    "intuition",
                    "global harmony",
                    "spiritual connection",
                    "ecological wisdom"
                ],
                "worldview": (
                    "The world is a single, interconnected, living organism. "
                    "Everything affects everything else. Intuition and holistic "
                    "knowing complement rational analysis. We are all one."
                ),
                "motivations": [
                    "collective good",
                    "ecological harmony",
                    "evolution of consciousness",
                    "healing the whole",
                    "unity and connection"
                ],
                "fears": [
                    "isolation from the whole",
                    "losing connection",
                    "fragmentation"
                ],
                "typical_behaviors": [
                    "holistic thinking",
                    "intuitive decision-making",
                    "bridging diverse perspectives",
                    "working for collective evolution",
                    "balancing individual and collective"
                ],
                "language_patterns": [
                    "we are all connected",
                    "feel into this",
                    "the system wants to evolve",
                    "what serves the whole?",
                    "consciousness is awakening"
                ],
                "transition_triggers": [
                    "unknown - theoretical stage",
                    "continued evolution of consciousness"
                ],
                "regression_triggers": [
                    "being too far ahead of others",
                    "spiritual bypassing",
                    "disconnection from practical reality"
                ]
            }
        }
    ]
}


def seed_spiral_dynamics(db_session):
    """
    Seed the Spiral Dynamics framework and all stages into the database.
    """
    from app.models.framework import DevelopmentalFramework, FrameworkStage

    # Create the framework
    framework = DevelopmentalFramework(
        code=SPIRAL_DYNAMICS["code"],
        name=SPIRAL_DYNAMICS["name"],
        description=SPIRAL_DYNAMICS["description"],
        author=SPIRAL_DYNAMICS["author"],
        is_hierarchical=SPIRAL_DYNAMICS["is_hierarchical"],
        config=SPIRAL_DYNAMICS["config"],
        is_active=True
    )
    db_session.add(framework)
    db_session.flush()

    # Create all stages
    for stage_data in SPIRAL_DYNAMICS["stages"]:
        stage = FrameworkStage(
            framework_id=framework.id,
            code=stage_data["code"],
            name=stage_data["name"],
            description=stage_data["description"],
            ordinal=stage_data["ordinal"],
            color=stage_data["color"],
            characteristics=stage_data["characteristics"]
        )
        db_session.add(stage)

    db_session.commit()
    print(f"Seeded Spiral Dynamics framework with {len(SPIRAL_DYNAMICS['stages'])} stages")
