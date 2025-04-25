def MatchProfiles(profile1, profile2):
    matched = True
    # gender check
    test_areas = ["gender","field_of_study","class_year"]
    
    for area in test_areas:
        if profile1["filters"][area] != 'any':
            if profile2[area] != profile1["filters"][area]:
                matched = False

        if profile2["filters"][area] != 'any':
            if profile1[area] != profile2["filters"][area]:
                matched = False

    return matched
