"""
MECE Life Domain Hierarchy Seed Data

7 top-level domains covering all aspects of life:
1. SELF - Internal experience and personal development
2. RELATIONSHIPS - Connections with others
3. WORK - Professional life and career
4. RESOURCES - Material, financial, and temporal resources
5. HEALTH - Physical and mental wellbeing
6. ENVIRONMENT - External context and surroundings
7. MEANING - Purpose, spirituality, and fulfillment
"""

DOMAIN_HIERARCHY = {
    "SELF": {
        "name": "Self",
        "description": "Internal experience, identity, and personal development",
        "metadata": {"color": "#9B59B6", "icon": "user"},
        "subdomains": {
            "IDENTITY": {
                "name": "Identity & Values",
                "description": "Core sense of who you are and what you stand for",
                "subdomains": {
                    "VALUES": {
                        "name": "Core Values",
                        "description": "Fundamental beliefs that guide decisions and behavior"
                    },
                    "SELF_CONCEPT": {
                        "name": "Self-Concept",
                        "description": "How you perceive and define yourself"
                    },
                    "AUTHENTICITY": {
                        "name": "Authenticity",
                        "description": "Alignment between inner truth and outer expression"
                    }
                }
            },
            "EMOTIONAL": {
                "name": "Emotional Life",
                "description": "Experience and management of emotions",
                "subdomains": {
                    "AWARENESS": {
                        "name": "Emotional Awareness",
                        "description": "Ability to recognize and name emotions"
                    },
                    "REGULATION": {
                        "name": "Emotional Regulation",
                        "description": "Capacity to manage emotional responses"
                    },
                    "EXPRESSION": {
                        "name": "Emotional Expression",
                        "description": "Healthy communication of emotions"
                    }
                }
            },
            "COGNITIVE": {
                "name": "Mental & Cognitive",
                "description": "Thinking patterns and mental development",
                "subdomains": {
                    "MINDSET": {
                        "name": "Mindset",
                        "description": "Mental models and thinking patterns"
                    },
                    "LEARNING": {
                        "name": "Learning",
                        "description": "Continuous acquisition of knowledge and skills"
                    },
                    "CREATIVITY": {
                        "name": "Creativity",
                        "description": "Creative thinking and expression"
                    }
                }
            },
            "BEHAVIORAL": {
                "name": "Habits & Behavior",
                "description": "Patterns of action and self-discipline",
                "subdomains": {
                    "HABITS": {
                        "name": "Habits",
                        "description": "Daily routines and automatic behaviors"
                    },
                    "DISCIPLINE": {
                        "name": "Discipline",
                        "description": "Self-control and willpower"
                    },
                    "PRESENCE": {
                        "name": "Presence",
                        "description": "Mindfulness and present-moment awareness"
                    }
                }
            }
        }
    },
    "RELATIONSHIPS": {
        "name": "Relationships",
        "description": "Connections and interactions with other people",
        "metadata": {"color": "#E74C3C", "icon": "users"},
        "subdomains": {
            "INTIMATE": {
                "name": "Intimate/Romantic",
                "description": "Primary romantic and sexual relationships",
                "subdomains": {
                    "PARTNERSHIP": {
                        "name": "Partnership",
                        "description": "Quality of primary romantic relationship"
                    },
                    "INTIMACY": {
                        "name": "Intimacy",
                        "description": "Emotional and physical closeness"
                    },
                    "COMMITMENT": {
                        "name": "Commitment",
                        "description": "Long-term relationship building and maintenance"
                    }
                }
            },
            "FAMILY": {
                "name": "Family",
                "description": "Relationships with family members",
                "subdomains": {
                    "ORIGIN": {
                        "name": "Family of Origin",
                        "description": "Relationships with parents and siblings"
                    },
                    "EXTENDED": {
                        "name": "Extended Family",
                        "description": "Connections with broader family network"
                    },
                    "PARENTING": {
                        "name": "Parenting",
                        "description": "Relationship with and raising of children"
                    }
                }
            },
            "SOCIAL": {
                "name": "Social & Friends",
                "description": "Friendships and social connections",
                "subdomains": {
                    "CLOSE_FRIENDS": {
                        "name": "Close Friends",
                        "description": "Deep, meaningful friendships"
                    },
                    "COMMUNITY": {
                        "name": "Community",
                        "description": "Broader social circles and belonging"
                    },
                    "NETWORKING": {
                        "name": "Networking",
                        "description": "Professional and interest-based connections"
                    }
                }
            },
            "PROFESSIONAL": {
                "name": "Professional Relationships",
                "description": "Work-related interpersonal dynamics",
                "subdomains": {
                    "COLLEAGUES": {
                        "name": "Colleagues",
                        "description": "Day-to-day work relationships"
                    },
                    "MENTORSHIP": {
                        "name": "Mentorship",
                        "description": "Mentor and mentee relationships"
                    },
                    "LEADERSHIP": {
                        "name": "Leadership",
                        "description": "Leading others and being led"
                    }
                }
            }
        }
    },
    "WORK": {
        "name": "Work & Career",
        "description": "Professional life and contribution through work",
        "metadata": {"color": "#F39C12", "icon": "briefcase"},
        "subdomains": {
            "CAREER": {
                "name": "Career Path",
                "description": "Long-term professional trajectory",
                "subdomains": {
                    "DIRECTION": {
                        "name": "Career Direction",
                        "description": "Vision and trajectory for professional life"
                    },
                    "ADVANCEMENT": {
                        "name": "Advancement",
                        "description": "Growth, promotions, and progression"
                    },
                    "SKILLS": {
                        "name": "Professional Skills",
                        "description": "Development of work-related competencies"
                    }
                }
            },
            "PERFORMANCE": {
                "name": "Work Performance",
                "description": "Quality and impact of work output",
                "subdomains": {
                    "PRODUCTIVITY": {
                        "name": "Productivity",
                        "description": "Output and efficiency in work"
                    },
                    "QUALITY": {
                        "name": "Quality",
                        "description": "Excellence and standards in work"
                    },
                    "IMPACT": {
                        "name": "Impact",
                        "description": "Results and contribution to organization"
                    }
                }
            },
            "ENGAGEMENT": {
                "name": "Work Engagement",
                "description": "Relationship with work itself",
                "subdomains": {
                    "SATISFACTION": {
                        "name": "Job Satisfaction",
                        "description": "Fulfillment from work"
                    },
                    "MOTIVATION": {
                        "name": "Motivation",
                        "description": "Drive and engagement with work"
                    },
                    "BALANCE": {
                        "name": "Work-Life Balance",
                        "description": "Integration of work with rest of life"
                    }
                }
            }
        }
    },
    "RESOURCES": {
        "name": "Resources",
        "description": "Material, financial, and temporal assets",
        "metadata": {"color": "#27AE60", "icon": "wallet"},
        "subdomains": {
            "FINANCIAL": {
                "name": "Financial",
                "description": "Money and financial health",
                "subdomains": {
                    "INCOME": {
                        "name": "Income",
                        "description": "Earning capacity and cash flow"
                    },
                    "WEALTH": {
                        "name": "Wealth",
                        "description": "Assets and net worth accumulation"
                    },
                    "SECURITY": {
                        "name": "Financial Security",
                        "description": "Stability, safety net, and protection"
                    },
                    "FREEDOM": {
                        "name": "Financial Freedom",
                        "description": "Independence and optionality from money"
                    }
                }
            },
            "TEMPORAL": {
                "name": "Time",
                "description": "Management and use of time",
                "subdomains": {
                    "MANAGEMENT": {
                        "name": "Time Management",
                        "description": "How time is allocated and used"
                    },
                    "AUTONOMY": {
                        "name": "Time Autonomy",
                        "description": "Control over your own schedule"
                    },
                    "EFFICIENCY": {
                        "name": "Time Efficiency",
                        "description": "Effective use of available time"
                    }
                }
            },
            "MATERIAL": {
                "name": "Material",
                "description": "Physical possessions and tools",
                "subdomains": {
                    "POSSESSIONS": {
                        "name": "Possessions",
                        "description": "Physical belongings and their management"
                    },
                    "TOOLS": {
                        "name": "Tools",
                        "description": "Resources that enable productivity"
                    },
                    "SPACE": {
                        "name": "Physical Space",
                        "description": "Home, office, and personal spaces"
                    }
                }
            }
        }
    },
    "HEALTH": {
        "name": "Health",
        "description": "Physical and mental wellbeing",
        "metadata": {"color": "#3498DB", "icon": "heart"},
        "subdomains": {
            "PHYSICAL": {
                "name": "Physical Health",
                "description": "Body and physical functioning",
                "subdomains": {
                    "FITNESS": {
                        "name": "Fitness",
                        "description": "Exercise, strength, and physical capacity"
                    },
                    "NUTRITION": {
                        "name": "Nutrition",
                        "description": "Diet and eating habits"
                    },
                    "SLEEP": {
                        "name": "Sleep",
                        "description": "Rest, recovery, and sleep quality"
                    },
                    "VITALITY": {
                        "name": "Vitality",
                        "description": "Overall energy and wellness"
                    }
                }
            },
            "MENTAL": {
                "name": "Mental Health",
                "description": "Psychological wellbeing",
                "subdomains": {
                    "STABILITY": {
                        "name": "Psychological Stability",
                        "description": "Mental health baseline and functioning"
                    },
                    "RESILIENCE": {
                        "name": "Resilience",
                        "description": "Ability to recover from setbacks"
                    },
                    "WELLBEING": {
                        "name": "Mental Wellbeing",
                        "description": "Overall psychological health and flourishing"
                    }
                }
            },
            "PREVENTIVE": {
                "name": "Preventive Care",
                "description": "Proactive health management",
                "subdomains": {
                    "CHECKUPS": {
                        "name": "Health Checkups",
                        "description": "Regular health monitoring and screenings"
                    },
                    "RISK_MANAGEMENT": {
                        "name": "Risk Management",
                        "description": "Addressing and mitigating health risks"
                    },
                    "LONGEVITY": {
                        "name": "Longevity",
                        "description": "Long-term health and lifespan optimization"
                    }
                }
            }
        }
    },
    "ENVIRONMENT": {
        "name": "Environment",
        "description": "External context and surroundings",
        "metadata": {"color": "#1ABC9C", "icon": "globe"},
        "subdomains": {
            "PHYSICAL_ENV": {
                "name": "Physical Environment",
                "description": "Physical spaces and locations",
                "subdomains": {
                    "HOME": {
                        "name": "Home Environment",
                        "description": "Quality of living space"
                    },
                    "WORKSPACE": {
                        "name": "Workspace",
                        "description": "Quality of work environment"
                    },
                    "LOCALITY": {
                        "name": "Locality",
                        "description": "Neighborhood, city, and geographic location"
                    }
                }
            },
            "SOCIAL_ENV": {
                "name": "Social Environment",
                "description": "Social and cultural context",
                "subdomains": {
                    "CULTURE": {
                        "name": "Cultural Context",
                        "description": "Cultural environment and influences"
                    },
                    "COMMUNITY_ENV": {
                        "name": "Community Environment",
                        "description": "Quality of local community"
                    },
                    "INSTITUTIONS": {
                        "name": "Institutions",
                        "description": "Relationship with societal institutions"
                    }
                }
            },
            "DIGITAL_ENV": {
                "name": "Digital Environment",
                "description": "Online and technology context",
                "subdomains": {
                    "DIGITAL_PRESENCE": {
                        "name": "Digital Presence",
                        "description": "Online identity and footprint"
                    },
                    "DIGITAL_WELLNESS": {
                        "name": "Digital Wellness",
                        "description": "Healthy relationship with technology"
                    },
                    "INFORMATION": {
                        "name": "Information Environment",
                        "description": "Quality of information inputs"
                    }
                }
            }
        }
    },
    "MEANING": {
        "name": "Meaning & Purpose",
        "description": "Existential and spiritual dimensions of life",
        "metadata": {"color": "#8E44AD", "icon": "star"},
        "subdomains": {
            "PURPOSE": {
                "name": "Purpose",
                "description": "Life mission and direction",
                "subdomains": {
                    "MISSION": {
                        "name": "Life Mission",
                        "description": "Core calling and life purpose"
                    },
                    "CONTRIBUTION": {
                        "name": "Contribution",
                        "description": "How you give back to others and the world"
                    },
                    "LEGACY": {
                        "name": "Legacy",
                        "description": "What you leave behind"
                    }
                }
            },
            "SPIRITUAL": {
                "name": "Spirituality",
                "description": "Connection to something greater",
                "subdomains": {
                    "BELIEFS": {
                        "name": "Spiritual Beliefs",
                        "description": "Spiritual or philosophical worldview"
                    },
                    "PRACTICE": {
                        "name": "Spiritual Practice",
                        "description": "Regular spiritual or contemplative practices"
                    },
                    "TRANSCENDENCE": {
                        "name": "Transcendence",
                        "description": "Connection to something larger than self"
                    }
                }
            },
            "FULFILLMENT": {
                "name": "Fulfillment",
                "description": "Overall life satisfaction",
                "subdomains": {
                    "LIFE_SATISFACTION": {
                        "name": "Life Satisfaction",
                        "description": "Overall contentment with life"
                    },
                    "GROWTH": {
                        "name": "Personal Growth",
                        "description": "Continuous evolution and development"
                    },
                    "INTEGRATION": {
                        "name": "Integration",
                        "description": "Wholeness and coherence across life"
                    }
                }
            }
        }
    }
}


def seed_domains(db_session):
    """
    Seed all domains into the database.

    Creates the full MECE hierarchy with proper parent-child relationships.
    """
    from app.models.domain import Domain

    def create_domain(code: str, data: dict, parent_id: str | None, level: int, ordinal: int) -> str:
        """Create a single domain and return its ID."""
        domain = Domain(
            code=code,
            name=data.get("name", code),
            description=data.get("description"),
            parent_id=parent_id,
            level=level,
            ordinal=ordinal,
            metadata_=data.get("metadata", {}),
            is_active=True
        )
        db_session.add(domain)
        db_session.flush()  # Get the ID
        return domain.id

    def process_hierarchy(hierarchy: dict, parent_id: str | None, parent_code: str, level: int):
        """Recursively process domain hierarchy."""
        for ordinal, (code, data) in enumerate(hierarchy.items()):
            full_code = f"{parent_code}.{code}" if parent_code else code

            # Create this domain
            domain_id = create_domain(full_code, data, parent_id, level, ordinal)

            # Process subdomains if present
            if "subdomains" in data:
                process_hierarchy(data["subdomains"], domain_id, full_code, level + 1)

    # Start processing from top level
    process_hierarchy(DOMAIN_HIERARCHY, None, "", 0)
    db_session.commit()

    print(f"Seeded domain hierarchy successfully")
