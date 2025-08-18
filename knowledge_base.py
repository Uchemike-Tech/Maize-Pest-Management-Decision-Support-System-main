# knowledge_base.py

def get_recommendation(diagnosis):
    """Returns an IPM recommendation based on the diagnosis."""

    recommendations = {
        'Fall Armyworm': {
            'description': 'A destructive pest that feeds on maize leaves, whorls, and cobs, causing significant yield loss.',
            'cultural': '1. Plant early to avoid peak infestation periods. \n2. Use push-pull intercropping with Napier grass and Desmodium.',
            'biological': '1. Encourage natural enemies like wasps and predatory bugs. \n2. Apply biopesticides based on Bacillus thuringiensis (Bt).',
            'chemical': 'Use recommended insecticides only when infestation reaches economic threshold (e.g., >20% of plants infested). Rotate chemical classes to avoid resistance.'
        },
        'Maize Stem Borer': {
            'description': 'Larvae bore into maize stems, causing "dead heart" in young plants and stem breakage in older ones.',
            'cultural': '1. Remove and destroy crop residues after harvest. \n2. Use tolerant maize varieties.',
            'biological': '1. Release of parasitic wasps like Cotesia flavipes. \n2. Use of entomopathogenic nematodes.',
            'chemical': 'Apply granular insecticides to the whorl at the vegetative stage if infestation is high.'
        },
        'Northern Leaf Blight': {
            'description': 'A fungal disease causing long, elliptical, grayish-green or tan lesions on leaves, reducing photosynthesis and yield.',
            'cultural': '1. Practice crop rotation with non-host crops. \n2. Use resistant hybrids. \n3. Ensure good field drainage to reduce humidity.',
            'biological': 'No established biological control, focus on cultural and chemical methods.',
            'chemical': 'Apply foliar fungicides when lesions first appear on lower leaves, especially if weather is cool and wet.'
        },
        'Maize Lethal Necrosis': {
            'description': 'A viral disease causing severe chlorosis, leaf mottling, and "dead heart" symptoms, often leading to plant death.',
            'cultural': '1. Use certified, disease-free seeds. \n2. Control insect vectors like thrips and leafhoppers. \n3. Practice strict field hygiene and remove infected plants immediately.',
            'biological': 'No direct biological control for the virus.',
            'chemical': 'Use insecticides to manage vector populations.'
        },
        'Drought Stress': {
            'description': 'Caused by insufficient water, leading to wilting, stunted growth, and poor kernel development.',
            'cultural': '1. Implement water conservation techniques like mulching. \n2. Plant drought-tolerant maize varieties. \n3. Optimize planting density to reduce water competition.',
            'biological': 'Not applicable.',
            'chemical': 'Not applicable.'
        },
        'Healthy': {
            'description': 'The plant shows no significant signs of pest or disease stress.',
            'cultural': 'Continue good agronomic practices, including regular monitoring, balanced fertilization, and proper water management to maintain plant health.',
            'biological': 'N/A',
            'chemical': 'N/A'
        }
    }
    return recommendations.get(diagnosis, {
        'description': 'No information available for this diagnosis.',
        'cultural': '', 'biological': '', 'chemical': ''
    })