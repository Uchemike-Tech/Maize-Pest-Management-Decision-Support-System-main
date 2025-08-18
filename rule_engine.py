# rule_engine.py

def get_rule_based_diagnosis(data):
    """
    Applies a set of rules to diagnose maize issues.
    Returns a diagnosis string or None if no rule matches.
    """
    # Rule 1: Definitive Stem Borer sign
    if data['Symptom_Stem_Boring'] == 1 and data['Crop_Stage'] != 'Seedling':
        return 'Maize Stem Borer'

    # Rule 2: Classic sign of heavy Fall Armyworm infestation at the right stage
    if data['Symptom_Holes_in_Leaves'] == 1 and data['Crop_Stage'] in ['Vegetative', 'Flowering']:
        return 'Fall Armyworm'

    # Rule 3: Clear drought conditions
    if data['Symptom_Wilting'] == 1 and data['Temperature'] > 33 and data['Rainfall_mm'] < 5:
        return 'Drought Stress'
        
    # If no specific rule matches, return None to defer to the ML model
    return None