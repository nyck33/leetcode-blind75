// File: ptxTester.cu
#include <cuda_runtime_api.h>
#include <iostream>
#include <cuda.h>

extern "C" void computeCovarianceMatrixFromPTX(double* S, double* R, double* Sigma, int sRows, int sCols, int rCols) {
    CUmodule cuModule;
    CUfunction cuFunction;
    cuInit(0);
    CUdevice cuDevice;
    cuDeviceGet(&cuDevice, 0);
    CUcontext cuContext;
    cuCtxCreate(&cuContext, 0, cuDevice);
    
    // PTX source embedded directly in the code, truncated for brevity
    const char *ptxSource = R"ptx(
        // PTX source should start here, with the entire kernel code as a single string
        .version 6.3
        .target sm_75
        .address_size 64

        .visible .entry _Z14matrixMultiplyPdS_S_iii(
            .param .u64 _Z14matrixMultiplyPdS_S_iii_param_0,
            .param .u64 _Z14matrixMultiplyPdS_S_iii_param_1,
            .param .u64 _Z14matrixMultiplyPdS_S_iii_param_2,
            .param .u32 _Z14matrixMultiplyPdS_S_iii_param_3,
            .param .u32 _Z14matrixMultiplyPdS_S_iii_param_4,
            .param .u32 _Z14matrixMultiplyPdS_S_iii_param_5
        )
        {
            .reg .pred 	%p<9>;
            .reg .b32 	%r<39>;
            .reg .b64 	%rd<30>;
            .reg .f64 	%fd<30>;

            // %bb.0:                               // %entry
            ld.param.u32 	%r20, [_Z14matrixMultiplyPdS_S_iii_param_5];
            ld.param.u32 	%r21, [_Z14matrixMultiplyPdS_S_iii_param_3];
            mov.u32 	%r22, %ctaid.y;
            mov.u32 	%r23, %ntid.y;
            mov.u32 	%r24, %tid.y;
            mad.lo.s32 	%r1, %r22, %r23, %r24;
            mov.u32 	%r25, %ctaid.x;
            mov.u32 	%r26, %ntid.x;
            mov.u32 	%r27, %tid.x;
            mad.lo.s32 	%r2, %r25, %r26, %r27;
            setp.ge.s32 	%p1, %r1, %r21;
            setp.ge.s32 	%p2, %r2, %r20;
            or.pred  	%p3, %p1, %p2;
            @%p3 bra 	$L__BB0_9;
            // %bb.1:                               // %for.cond.preheader
            ld.param.u32 	%r19, [_Z14matrixMultiplyPdS_S_iii_param_4];
            ld.param.u64 	%rd11, [_Z14matrixMultiplyPdS_S_iii_param_2];
            cvta.to.global.u64 	%rd1, %rd11;
            setp.lt.s32 	%p4, %r19, 1;
            mov.f64 	%fd28, 0d0000000000000000;
            @%p4 bra 	$L__BB0_8;
            // %bb.2:                               // %for.body.lr.ph
            ld.param.u64 	%rd10, [_Z14matrixMultiplyPdS_S_iii_param_0];
            ld.param.u64 	%rd12, [_Z14matrixMultiplyPdS_S_iii_param_1];
            cvta.to.global.u64 	%rd2, %rd12;
            cvta.to.global.u64 	%rd3, %rd10;
            mul.lo.s32 	%r3, %r1, %r19;
            and.b32  	%r35, %r19, 3;
            setp.lt.u32 	%p5, %r19, 4;
            mov.f64 	%fd28, 0d0000000000000000;
            mov.u32 	%r34, 0;
            @%p5 bra 	$L__BB0_5;
            // %bb.3:                               // %for.body.lr.ph.new
            and.b32  	%r34, %r19, -4;
            shl.b32 	%r6, %r20, 2;
            shl.b32 	%r7, %r20, 1;
            mul.lo.s32 	%r8, %r20, 3;
            mul.wide.s32 	%rd13, %r3, 8;
            add.s64 	%rd14, %rd13, %rd3;
            add.s64 	%rd29, %rd14, 16;
            mov.f64 	%fd28, 0d0000000000000000;
            mov.u32 	%r37, %r2;
            mov.u32 	%r38, %r34;
            $L__BB0_4:                              // %for.body
                                                    // =>This Inner Loop Header: Depth=1
            ld.global.f64 	%fd12, [%rd29+-16];
            mul.wide.s32 	%rd15, %r37, 8;
            add.s64 	%rd16, %rd2, %rd15;
            ld.global.f64 	%fd13, [%rd16];
            fma.rn.f64 	%fd14, %fd12, %fd13, %fd28;
            ld.global.f64 	%fd15, [%rd29+-8];
            add.s32 	%r29, %r20, %r37;
            mul.wide.s32 	%rd17, %r29, 8;
            add.s64 	%rd18, %rd2, %rd17;
            ld.global.f64 	%fd16, [%rd18];
            fma.rn.f64 	%fd17, %fd15, %fd16, %fd14;
            ld.global.f64 	%fd18, [%rd29];
            add.s32 	%r30, %r7, %r37;
            mul.wide.s32 	%rd19, %r30, 8;
            add.s64 	%rd20, %rd2, %rd19;
            ld.global.f64 	%fd19, [%rd20];
            fma.rn.f64 	%fd20, %fd18, %fd19, %fd17;
            ld.global.f64 	%fd21, [%rd29+8];
            add.s32 	%r31, %r8, %r37;
            mul.wide.s32 	%rd21, %r31, 8;
            add.s64 	%rd22, %rd2, %rd21;
            ld.global.f64 	%fd22, [%rd22];
            fma.rn.f64 	%fd28, %fd21, %fd22, %fd20;
            add.s32 	%r38, %r38, -4;
            add.s32 	%r37, %r37, %r6;
            add.s64 	%rd29, %rd29, 32;
            setp.eq.s32 	%p6, %r38, 0;
            @%p6 bra 	$L__BB0_5;
            bra.uni 	$L__BB0_4;
            $L__BB0_5:                              // %for.cond.cleanup.loopexit.unr-lcssa
            setp.eq.s32 	%p7, %r35, 0;
            @%p7 bra 	$L__BB0_8;
            // %bb.6:                               // %for.body.epil.preheader
            mad.lo.s32 	%r36, %r34, %r20, %r2;
            add.s32 	%r32, %r34, %r3;
            mul.wide.s32 	%rd23, %r32, 8;
            add.s64 	%rd28, %rd3, %rd23;
            $L__BB0_7:                              // %for.body.epil
                                                    // =>This Inner Loop Header: Depth=1
            .pragma "nounroll";
            ld.global.f64 	%fd23, [%rd28];
            mul.wide.s32 	%rd24, %r36, 8;
            add.s64 	%rd25, %rd2, %rd24;
            ld.global.f64 	%fd24, [%rd25];
            fma.rn.f64 	%fd28, %fd23, %fd24, %fd28;
            add.s32 	%r36, %r36, %r20;
            add.s64 	%rd28, %rd28, 8;
            add.s32 	%r35, %r35, -1;
            setp.ne.s32 	%p8, %r35, 0;
            @%p8 bra 	$L__BB0_7;
            $L__BB0_8:                              // %for.cond.cleanup
            mad.lo.s32 	%r33, %r1, %r20, %r2;
            mul.wide.s32 	%rd26, %r33, 8;
            add.s64 	%rd27, %rd1, %rd26;
            st.global.f64 	[%rd27], %fd28;
            $L__BB0_9:                              // %if.end
            ret;
                                                    // -- End function
        }
    )ptx";

    // Load the PTX code into a module
    cuModuleLoadData(&cuModule, ptxSource);
    // Obtain a handle to the kernel function
    cuModuleGetFunction(&cuFunction, cuModule, "_Z14matrixMultiplyPdS_S_iii");

    void* args[] = { &S, &R, &Sigma, &sRows, &sCols, &rCols };

    // Define grid and block dimensions based on the original CUDA code logic
    int threadsPerBlock = 256; // Number of threads per block
    int blockSize = 16; // Block size for x and y dimensions
    int numBlocksX = (sCols + blockSize - 1) / blockSize;
    int numBlocksY = (sRows + blockSize - 1) / blockSize;

    // Launch the kernel
    cuLaunchKernel(cuFunction,
                   numBlocksX, numBlocksY, 1, // Adjusted Grid dimensions
                   blockSize, blockSize, 1, // Block dimensions
                   0, NULL, // Shared memory and stream
                   args, NULL); // Kernel arguments and extra options

    // Synchronize to wait for kernel completion
    cuCtxSynchronize();
    // Clean up
    cuCtxDestroy(cuContext);
}
