'''
create jobs for Fast Rotational Matching (FRM) alignment interactively
Created on Apr 2, 2013

@author: yuxiangchen
@lastchange: FF, May 2020
'''

from pytom.tools.files import checkFileExists

def create_job_frm():
    """
    create job interactively - xml file will be written
    """
    # Task 0
    # particle list
    print("1/10. Please enter the particle list(s) to be aligned. Multiple lists should be separated by a space.")
    print("(Note the wedge situation of the particles should be set.)")
    print("(It is strongly recommended that the absolute path should be given for all the particles.)")
    while True:
        pl_filenames = input('--> ')
        pl_filenames = pl_filenames.split(' ')
        for pl_filename in pl_filenames:
            if not checkFileExists(pl_filename):
                print("Particle list does not exist. Please enter again.")
                break
        else:
            break
    
    # reference
    print("2/10. Please enter the file name of the reference.")
    print("(Note it should be the same size as the particles.)")
    while True:
        ref_filename = input('--> ')
        if checkFileExists(ref_filename):
            break
        else:
            print("Reference does not exist. Please enter again.")
    
    # mask
    print("3/10. Please enter the file name of the mask.")
    print("(Note it should be the same size as the reference.)")
    while True:
        mask_filename = input('--> ')
        if checkFileExists(mask_filename):
            break
        else:
            print("Mask does not exist. Please enter again.")
    
    # starting frequency
    print("4/10. Please enter the starting frequency (in pixel) of the alignment procedure.")
    print("(This is equal to apply the low-pass filter to the reference.)")
    while True:
        freq = input('--> ')
        
        try:
            freq = int(freq)
            if freq > 0:
                break
            else:
                raise Exception()
        except:
            print("The starting frequency should be a positive integer. Please enter again.")
    
    # peak offset
    print("5/10. Please enter the maximal distance allowed (in pixel) to shift the reference.")
    print("(This field is used to prevent shifting the volume out-of-frame and reduce the search space.)")
    while True:
        peak_offset = input('--> ')
        
        try:
            peak_offset = int(peak_offset)
            if peak_offset > 0:
                break
            else:
                raise Exception()
        except:
            print("The peak offset should be a positive integer. Please enter again.")
    
    # number of iterations
    print("6/10. Please enter the number of iterations to run.")
    while True:
        niter = input('--> ')
        
        try:
            niter = int(niter)
            if niter > 0:
                break
            else:
                raise Exception()
        except:
            print("The number of iterations should be a positive integer. Please enter again.")

    # binning
    print("7/10. Please enter the binning factor (>=1, default is 1).")
    while True:
        binning = input('--> ')
        
        try:
            if len(binning) == 0:
                binning = 1
            else:
                binning = int(binning)
            if binning >= 1:
                break
            else:
                raise Exception()
        except:
            print("The Binning factor should be 1 or greater. Please enter again.")
            
    
    # pixel size
    print("8/10. Please enter the pixel size (in Angstrom).")
    while True:
        pixel_size = input('--> ')
        
        try:
            pixel_size = float(pixel_size)
            if pixel_size > 0:
                break
            else:
                raise Exception()
        except:
            print("The pixel size should be a positive number. Please enter again.")
    
    # adaptive resolution
    print("9/10. Please enter the adaptive resolution to be included (in percentage, default is 0).")
    while True:
        adaptive_res = input('--> ')
        
        try:
            if len(adaptive_res) == 0:
                adaptive_res = 0.0
            else:
                adaptive_res = float(adaptive_res)
            if adaptive_res >= 0 and adaptive_res < 1:
                break
            else:
                raise Exception()
        except:
            print("The adaptive resolution should be a number in the range 0-1. Please enter again.")
            
    # FSC criterion
    print("10/10. Please enter the FSC criterion to use (default is 0.5).")
    while True:
        fsc = input('--> ')
        
        try:
            if len(fsc) == 0:
                fsc = 0.5
            else:
                fsc = float(fsc)
            if fsc > 0 and fsc < 1:
                break
            else:
                raise Exception()
        except:
            print("The FSC criterion should be a number in the range 0-1. Please enter again.")
    
    # write to the disk
    print("Finished. Save as:")
    while True:
        output = input('--> ')
        try:
            f = open(output, 'w')
            f.write(f"<FRMJob Destination='.' BandwidthRange='[4, 64]' Frequency='{freq:d}' MaxIterations='{niter:d}' PeakOffset='{peak_offset:d}' AdaptiveResolution='{adaptive_res:.2f}' FSC='{fsc:.2f}' binning='{binning:d}'>\n")
            #f.write("    <Reference PreWedge='' File='%s' Weighting=''>\n      <ParticleList Path='/'/>\n    </Reference>\n" % ref_filename)
            f.write("    <Reference PreWedge='' File='%s' Weighting=''>\n          </Reference>\n" % ref_filename)
            f.write("    <Mask Filename='%s' isSphere='True'/>\n" % mask_filename)
            f.write("    <SampleInformation PixelSize='%.2f' ParticleDiameter='1'/>\n" % pixel_size)
            for pl_filename in pl_filenames:
                f.write("    <ParticleListLocation Path='%s'/>\n" % pl_filename)
            f.write("</FRMJob>")
        except:
            print("Something is wrong during writing. Please enter again the file name.")
        finally:
            f.close()
            break
    

def create_job_gfrm():
    # Task 1
    raise RuntimeError("Not implemented yet.")

def create_job_wf():
    # Task 2
    raise RuntimeError("Not implemented yet.")

def create_job_gwf():
    # Task 3
    raise RuntimeError("Not implemented yet.")


if __name__ == '__main__':
    print("This is a guide of creating the job file for alignment tasks using spherical harmonics (fast rotational matching).")
    print()
    print("For detail, please check the documentation:")
    print("Or the paper: 'Fast and accurate reference-free alignment of subtomograms, Y. Chen et al., Journal of Structural Biology, 2013.'")
    print()
    print("Please choose the task style:")
    print("[0] Subtomogram alignment without Wiener filter (script name: FRMAlignment.py)")
    print("[1] Subtomogram alignment of gold-standard FSC without Wiener filter (script name: GFRMAlignment.py)")
    print("[2] Subtomogram alignment with Wiener filter (script name: WienerFilterAlignment.py)")
    print("[3] Subtomogram alignment of gold-standard FSC with Wiener filter (script name: GWienerFilterAlignment.py)")
    

    while True:
        task_style = input('--> ')
        
        try:
            task_style = int(task_style)
            if task_style in range(0,4):
                break
            else:
                raise Exception()
        except:
            print("Please enter a number of 0-3.")
    
    if task_style == 0:
        create_job_frm()
    elif task_style == 1:
        create_job_gfrm()
    elif task_style == 2:
        create_job_wf()
    elif task_style == 3:
        create_job_gwf()
    else:
        raise RuntimeError("The task number should only be in the range of 0-3. Exit.")
    
