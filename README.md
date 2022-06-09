# -motion-artifacts!


SPNet output with different loss function

Test Image with artefacts in depth dataset

1) GT Image ............... 2) Depth ...................... 3) RGB 

![GT](/GT_1500.png)....![depth](images/test/corrupted_depth_1500.png).....![rgb](images/test/RGB_1500.png)


Introduce artefacts in RGB 

1).  GT Image  .............. 2)  With SSIM Loss. ............ 3)      With MSE Loss  ............. 4) With Structure Loss (Original SPNet Loss) 

![GT](/GT_1500.png) ....... ![SSIM](/corrupted_RGB_1500_SSIMLoss.png) ......... ![MSE](/corrupted_RGB_1500_MSELoss.png). ......... ![Structure](/corrupted_RGB_1500_Structure_loss.png)


Introduce artefacts in depth

1). GT Image ...........  2) SSIM Loss ............  3) MSE Loss........... 4) Structure Loss........ 5) Perceptual Loss ...... 6) Perceptual Loss update


![GT](/GT_1500.png) ![SSIM](images/depth_noise/RGB_1500_SSIM_update.png) ![MSE](images/depth_noise/RGB_1500_MSE_update.png) ![Structure](images/depth_noise/RGB_1500_structure_update.png) ![Percept](images/depth_noise/RGB_1500_perceptual.png) ![Percept_Update](images/depth_noise/RGB_1500_perceptual_update.png)










