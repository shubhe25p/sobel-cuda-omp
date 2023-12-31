#!/bin/bash 
#SBATCH -N 1
#SBATCH -C gpu
#SBATCH -G 1
#SBATCH -q regular
#SBATCH -t 00:10:00
#SBATCH -A m3930
#SBATCH -J queue
#SBATCH --job-name=gpu-job
#SBATCH --output=gpu-job.o%j
#SBATCH --error=gpu-job.e%j

#
# note: you will need to modify below here to launch your specific program
# it is assumed your environment is set up properly for using the Cori GPUs
# prior to you launching this batch script
#
nblocks=(1 4 16 64 256 1024 4096)
nThreads=(32 64 128 256 512 1024)

for i in "${nblocks[@]}"; do
    for j in "${nThreads[@]}"; do
        echo "nblocks: $i, nThreads: $j"
        ncu --set default --section SourceCounters --metrics smsp__cycles_active.avg.pct_of_peak_sustained_elapsed,dram__throughput.avg.pct_of_peak_sustained_elapsed,gpu__time_duration.avg ../build/sobel_gpu $i $j
    done
done
# ncu --set default --section SourceCounters --metrics smsp__cycles_active.avg.pct_of_peak_sustained_elapsed,dram__throughput.avg.pct_of_peak_sustained_elapsed,gpu__time_duration.avg ./sobel_cpu_omp_offload



