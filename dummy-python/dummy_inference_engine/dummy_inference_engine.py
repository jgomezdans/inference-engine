import snappy

class dummy_inference_engine:

    def infer(self, coarse_res_brdf_descriptor, high_res_sdr, grd_sar_data, prior, optical_forward_operator_emulator,
              sar_forward_operator_emulator):
        print ('Inferring high resolution biophysical parameters')
        return snappy.Product('high_res_biophysical_params', 'high_res_biophysical_params', 1, 1)