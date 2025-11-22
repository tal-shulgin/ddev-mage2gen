#!/bin/bash
# This script runs INSIDE the container

cd /usr/app/src
echo "🔗 Setting up Core Library Symlinks..."

if [ -d "/usr/app/core_source/mage2gen" ]; then
    rm -rf mage2gen3 mage2gen4
    ln -s /usr/app/core_source/mage2gen ./mage2gen3
    ln -s /usr/app/core_source/mage2gen ./mage2gen4
    echo "✅ Linked 'core' fork."
else
    echo "⚠️  Core repository not found at /usr/app/core_source."
fi