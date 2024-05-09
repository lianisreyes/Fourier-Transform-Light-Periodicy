import numpy as np
import numpy.random as rand
import Scott_Princeton

def lorentzian(phi, gamma, x0 = 0.5):
    """
    Returns the solution of the lorenzian with the inputs: phi and gamma
    """
    return (gamma/((phi - x0)**2 + gamma**2))/np.pi


def generate(n_samples, n_bins, noise = True):
    """
    Generates Pulse Profile for generate_dummy 

    Inputs: 

    Outputs: Returns the pulses array for plotting, returns locs, returns gammas,  and amp variable  
    """
    max_subpulses = 6
    phi = np.linspace(0, 1, n_bins)
    pulses = np.zeros((n_samples, n_bins))
    locs = np.zeros((n_samples, max_subpulses + 1))
    gammas = np.copy(locs)
    amps = np.copy(locs)

    for i in range(n_samples):
        gamma = rand.choice(np.linspace(0.001, 0.05, 1000))
        pulse = lorentzian(phi, gamma)
        pulse /= max(pulse)
        pulse = np.zeros(1024)

        subpulses = rand.randint(0, max_subpulses + 1)
        subpulses = max_subpulses 
        #subpulses
        for j in range(subpulses):
            gamma_sub = rand.choice(np.linspace(0.001, 0.1, 1000))
            loc_sub = 0.5 + rand.normal(0, 0.1)
            #loc_sub = rand.choice(np.linspace(0.1, 0.9, 1024))
            subpulse = lorentzian(phi, gamma_sub,loc_sub)
            amp = rand.choice(np.linspace(0.1, 0.9))
            subpulse *= amp/max(subpulse)
            pulse += subpulse

            locs[i, j + 1] = loc_sub
            gammas[i, j + 1] = gamma_sub
            amps[i, j + 1] = amp

        if noise:
            rms = rand.choice(np.linspace(0.001, 0.3, 3000))
            pulse += rand.normal(0, rms, n_bins)

        pulses[i] = pulse
        locs[i, 0] = 0.5
        gammas[i, 0] = gamma
        amps[i, 0] = 1

    return pulses, locs, gammas, amps

def generate_dummy(n_samples, n_bins, noise = 0 , rms = 'false' ): 
    """
    Use: Generates Artificial data for testing 

    Inputs: number of sample, number of bins

    Output: Generates a pulse profile 
    """
    phi = np.linspace(0, 1, n_bins)
    pulses = np.zeros((n_samples, n_bins))
    locs = np.zeros(n_samples)

    for i in range(n_samples):

        pulse = np.zeros(1024)

        gamma_sub = rand.choice(np.linspace(0.001, 0.05, 1000))
        loc_sub = rand.choice(np.linspace(0.1, 0.9, 1024))
        subpulse = lorentzian(phi, gamma_sub,loc_sub)
        amp = rand.choice(np.linspace(0.1, 0.9))
        subpulse *= amp/max(subpulse)
        pulse += subpulse

        locs[i] = loc_sub
        pulses[i] = pulse
    
    if noise:
            pulse += rand.normal(0, rms, n_bins)

    return pulses, locs